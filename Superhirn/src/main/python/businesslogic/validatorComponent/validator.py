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
    def check_stone_input(self, input_strings, min_number, max_number):
        for element in input_strings:
            if not element.isdigit():
                raise self._validationError(f"Input must be integers between {min_number} and {max_number}!")

            if int(element) < int(min_number) or int(element) > int(max_number):
                raise self._validationError(f"Input must be integers between {min_number} and {max_number}!")

        return True

    # Validation for code length and whether the stones are in the set intervall or whether the entered value is a digit
    def check_code_input(self, input_strings, code_max_length, max_number):

        if len(input_strings) == code_max_length:
            return self.check_stone_input(input_strings, self._ruleBook().min_check_code, int(max_number))
        else:
            raise self._validationError(f"Input length must be equal to {code_max_length}!")

    def check_feedback_input(self, input_strings, code_max_length):
        if code_max_length >= len(input_strings) >= 0:
            if not input_strings:
                return True
            else:
                return self.check_stone_input(input_strings, self._ruleBook().min_feedback_colour,
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

    def check_game_state(self, board, user_role):
        win_condition_coder = user_role == self._role.Coder and board.attempt_counter > self._ruleBook().max_try
        lose_condition_coder = user_role == self._role.Coder and board.convert_stone_array_to_colour(
            board.create_board_stone_array(self._ruleBook().winning_feedback)) == board.convert_stone_array_to_colour(
            board.feedback)

        win_condition_rater = user_role == self._role.Rater and board.convert_stone_array_to_colour(
            board.create_board_stone_array(self._ruleBook().winning_feedback)) == board.convert_stone_array_to_colour(
            board.feedback)
        lose_condition_rater = user_role == self._role.Rater and board.attempt_counter > self._ruleBook().max_try

        if user_role == self._role.Coder:
            return self._gameState.Win.value if win_condition_coder else (
                self._gameState.Lose.value if lose_condition_coder else self._gameState.Undecided.value)
        elif user_role == self._role.Rater:
            return self._gameState.Lose.value if lose_condition_rater else (
                self._gameState.Win.value if win_condition_rater else self._gameState.Undecided.value)
