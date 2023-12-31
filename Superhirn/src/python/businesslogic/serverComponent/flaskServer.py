import random
from flask import Flask, request, jsonify

app = Flask(__name__)

active_games = {}


def generate_random_code(length, max_colour):
    return ''.join(str(random.randint(1, max_colour)) for _ in range(length))


def generate_feedback(code, guess):
    feedback = ""
    secret_marked = [False] * len(code)
    guess_marked = [False] * len(guess)

    for stone_code_position in range(len(code)):
        if code[stone_code_position] == guess[stone_code_position]:
            feedback += "8"
            secret_marked[stone_code_position] = guess_marked[stone_code_position] = True

    for stone_code_position in range(len(code)):
        if not secret_marked[stone_code_position]:
            for stone_guess_position in range(len(guess)):
                if (not guess_marked[stone_guess_position]
                        and code[stone_code_position]
                        == guess[stone_guess_position]):
                    feedback += "7"
                    guess_marked[stone_guess_position] = True
                    break

    feedback_list = list(feedback)
    random.shuffle(feedback_list)
    shuffled_feedback = ''.join(feedback_list)
    return shuffled_feedback


@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()

    game_id = data.get("gameid", 0)
    gamer_id = data.get("gamerid", "")
    positions = int(data.get("positions", 0))
    colors = int(data.get("colors", 0))
    guess = data.get("value", "")

    if game_id == 0:
        game_id = random.randint(1, 10000)
        code = generate_random_code(positions, colors)
        active_games[game_id] = code
        response_value = ""
    else:
        code = active_games.get(game_id, "")
        response_value = generate_feedback(code, guess)

    response_data = {
        "gameid": game_id,
        "gamerid": gamer_id,
        "positions": positions,
        "colors": colors,
        "value": response_value
    }

    return jsonify(response_data, 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
