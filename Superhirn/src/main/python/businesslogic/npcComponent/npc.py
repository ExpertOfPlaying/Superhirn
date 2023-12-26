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

    def create_code(self):
        if not self._board.guessed_code:
            self._board.code = "".join(
                str(random.randint(1, self._board.max_colour)) for _ in range(self._board.code_max_length))

    def create_feedback(self):
        print(self.board.convert_stone_array_to_colour(self.board.guessed_code))
        if self._board.code == self._board.guessed_code:
            self._board.feedback = "88888"
        elif self._board.attempt_counter <= 1:
            pass
