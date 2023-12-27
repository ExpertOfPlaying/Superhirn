import random
from src.main.python.entities.userComponent.roleEnum import Role


class NPC:
    def __init__(self, board):
        self._board = board
        self._role = self.opposite_role()

    @property
    def role(self):
        return self._role

    def opposite_role(self):
        return Role.Coder if self._board.game_mode == Role.Rater.value else Role.Rater

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def generate_code(self):
        if not self._board.guessed_code:
            self._board.code = "".join(
                str(random.randint(1, self._board.max_colour)) for _ in range(self._board.code_max_length))

    def generate_feedback(self):
        feedback = ""
        repeated_colours = []

        for code_position, code_stone in enumerate(self._board.code):
            for guess_position, guess_stone in enumerate(self._board.guessed_code):
                if code_position == guess_position and code_stone.colour == guess_stone.colour:
                    feedback += "8"
                    repeated_colours.append(guess_stone.colour)
                elif code_position != guess_position and code_stone.colour == guess_stone.colour:
                    if guess_stone.colour not in repeated_colours:
                        feedback += "7"
                        repeated_colours.append(guess_stone.colour)

        feedback_list = list(feedback)
        random.shuffle(list(feedback))
        shuffled_feedback = ''.join(feedback_list)
        self._board.feedback = shuffled_feedback
