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
        secret_marked = [False] * len(self._board.code)
        guess_marked = [False] * len(self._board.guessed_code)

        for stone_code_position in range(len(self._board.code)):
            if self._board.code[stone_code_position].colour == self._board.guessed_code[stone_code_position].colour:
                feedback += "8"
                secret_marked[stone_code_position] = guess_marked[stone_code_position] = True

        for stone_code_position in range(len(self._board.code)):
            if not secret_marked[stone_code_position]:
                for stone_guess_position in range(len(self._board.guessed_code)):
                    if not guess_marked[stone_guess_position] and self._board.code[stone_code_position].colour == self._board.guessed_code[stone_guess_position].colour:
                        feedback += "7"
                        guess_marked[stone_guess_position] = True
                        break

        feedback_list = list(feedback)
        random.shuffle(feedback_list)
        shuffled_feedback = ''.join(feedback_list)
        self._board.feedback = shuffled_feedback

    def generate_guess(self):
        # n^k (n = max_colours, k = code_max_length)
        # 2 ^ 4: 16 Rot Rot Grün Grün
        # 3 ^ 4: 81
        # 4 ^ 4: 256
        # 5 ^ 4: 625
        # 6 ^ 4: 1296
        # 7 ^ 4: 2401
        # 8 ^ 4: 4096
        # 2 ^ 5: 32
        # 3 ^ 5: 243
        # 4 ^ 5: 1024
        # 5 ^ 5: 3125
        # 6 ^ 5: 7776
        # 7 ^ 5: 16807
        # 8 ^ 5: 32768

        pass

    def generate_permutations(self):
        return pow(self._board.max_colour, self._board.code_max_length)
