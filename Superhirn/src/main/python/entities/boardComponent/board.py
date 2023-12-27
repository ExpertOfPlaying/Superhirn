from src.main.python.entities.stoneComponent.stone import Stone


class Board:
    def __init__(self, code_max_length, max_colour, attempt_counter, guessed_code, code, feedback, game_mode):
        self._code_max_length = code_max_length
        self._max_colour = max_colour
        self._max_attempts = 10
        self._attempt_counter = attempt_counter
        self._guessed_code = guessed_code
        self._guessed_code_list = []
        self._code = code
        self._feedback = feedback
        self._feedback_list = []
        self._game_mode = game_mode

    @staticmethod
    def create_board_stone_array(values):
        board_stones = [Stone(value) for value in values]
        return board_stones

    @staticmethod
    def convert_stone_array_to_colour(stone_array):
        if all(isinstance(inner_array, list) for inner_array in stone_array):
            colour_array = [[stone.colour for stone in inner_array] for inner_array in stone_array]
        else:
            colour_array = [stone.colour for stone in stone_array]

        return colour_array

    @property
    def code_max_length(self):
        return int(self._code_max_length)

    @property
    def max_colour(self):
        return int(self._max_colour)

    @property
    def max_attempts(self):
        return int(self._max_attempts)

    # für später, falls im lokalen Spiel max_attempts geändert werden sollte
    @max_attempts.setter
    def max_attempts(self, value):
        self._max_attempts = value

    @property
    def attempt_counter(self):
        return int(self._attempt_counter)

    @attempt_counter.setter
    def attempt_counter(self, value):
        self._attempt_counter = value

    @property
    def guessed_code(self):
        return self._guessed_code

    @guessed_code.setter
    def guessed_code(self, values):
        self._guessed_code = self.create_board_stone_array(values)
        self._guessed_code_list.append((self._attempt_counter, self._guessed_code))

    @property
    def guessed_code_list(self):
        return self._guessed_code_list

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, values):
        self._code = self.create_board_stone_array(values)

    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, values):
        self._feedback = self.create_board_stone_array(values)
        self._feedback_list.append((self._attempt_counter, self._feedback))

    @property
    def game_mode(self):
        return int(self._game_mode)

    @property
    def feedback_list(self):
        return self._feedback_list
