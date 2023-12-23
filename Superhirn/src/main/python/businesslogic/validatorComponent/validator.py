class Validator:
    def __init__(self, rule_book, validation_error, game_state, role):
        self._ruleBook = rule_book
        self._validationError = validation_error
        self._gameState = game_state
        self._role = role

    @property
    def validationError(self):
        return self._validationError

    # Validation for whether the stones are in the set intervall or whether the entered value is a digit
    def check_stone_input(self, input_string, min_number, max_number):
        if input_string.isdigit():
            stones = [int(num) for num in input_string]
            for stone in stones:
                if stone < int(min_number) or stone > int(max_number):
                    raise self._validationError(f"Input must be integers between {min_number} and {max_number}!")
            return True
        else:
            raise self._validationError(f"Input must be integers between {min_number} and {max_number}!")

    # Validation for code length and whether the stones are in the set intervall or whether the entered value is a digit
    def check_code_input(self, input_string, code_max_length, max_number):
        if len(input_string) == code_max_length:
            return self.check_stone_input(input_string, self._ruleBook().min_check_code, int(max_number))
        else:
            raise self._validationError(f"Input must be equal to {code_max_length}!")

    def check_feedback_input(self, input_string, code_max_length):
        if code_max_length >= len(input_string) > 0:
            if input_string == "":
                return True
            else:
                return self.check_stone_input(input_string, self._ruleBook().min_feedback_colour,
                                              self._ruleBook().max_feedback_colour)
        else:
            raise self._validationError(f"Input must be equal or less to {code_max_length}!")

    def set_digit_range(self, value, min_value, max_value):
        if value.isdigit():
            if min_value <= int(value) <= int(max_value):
                return True
            else:
                raise self._validationError(f"Input must be an integer between {min_value} or {max_value}!")
        else:
            raise self._validationError(f"Input must be an integer between {min_value} or {max_value}!")

    def check_max_code_length_input(self, code_max_length):
        return self.set_digit_range(code_max_length, self._ruleBook().min_code_length, self._ruleBook().max_code_length)

    def check_game_mode_input(self, game_mode):
        return self.set_digit_range(game_mode, self._ruleBook().min_game_mode, self._ruleBook().max_game_mode)

    def check_max_colour_input(self, max_colour):
        return self.set_digit_range(max_colour, self._ruleBook().min_colour, self._ruleBook().max_colour)

    def check_game_state(self, actual_attempt, guess, code):
        if self._role == self._role.Rater:
            if guess == code:
                return self._gameState.Win
            elif actual_attempt > self._ruleBook().max_try:
                return self._gameState.Lose
            else:
                return False
        if self._role == self._role.Coder:
            if guess == code:
                return self._gameState.Lose
            elif actual_attempt > self._ruleBook().max_try:
                return self._gameState.Win
            else:
                return False
