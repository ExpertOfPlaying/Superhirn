import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Speicher für aktive Spiele
active_games = {}


def generate_random_code(length, max_colour):
    return ''.join(str(random.randint(1, max_colour)) for _ in range(length))


def calculate_feedback(code, guess):
    feedback = []
    temp_code = list(code)
    for i in range(len(guess)):
        if guess[i] == code[i]:
            feedback.append("8")
            temp_code[i] = None

    for i in range(len(guess)):
        if guess[i] in temp_code:
            feedback.append("7")
            temp_code[temp_code.index(guess[i])] = None

    return ''.join(feedback)


@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()
    print("Empfangene Daten:", data)

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
        response_value = calculate_feedback(code, guess)

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
