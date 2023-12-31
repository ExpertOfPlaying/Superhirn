class RuleBook:
    def __init__(self):
        self._min_check_code = 1
        self._min_code_length = 4
        self._max_code_length = 5
        self._min_game_mode = 1
        self._max_game_mode = 2
        self._min_colour = 2
        self._max_colour = 8
        self._max_try = 10
        self._min_feedback_colour = 7
        self._max_feedback_colour = 8
        self._winning_feedback_4 = "8888"
        self._winning_feedback_5 = "88888"

    @property
    def min_check_code(self):
        return self._min_check_code

    @property
    def min_code_length(self):
        return self._min_code_length

    @property
    def max_code_length(self):
        return self._max_code_length

    @property
    def min_game_mode(self):
        return self._min_game_mode

    @property
    def max_game_mode(self):
        return self._max_game_mode

    @property
    def min_colour(self):
        return self._min_colour

    @property
    def max_colour(self):
        return self._max_colour

    @property
    def max_try(self):
        return self._max_try

    @max_try.setter
    def max_try(self, value):
        self._max_try = value

    @property
    def min_feedback_colour(self):
        return self._min_feedback_colour

    @property
    def max_feedback_colour(self):
        return self._max_feedback_colour

    @property
    def winning_feedback_4(self):
        return self._winning_feedback_4

    @property
    def winning_feedback_5(self):
        return self._winning_feedback_5
