class Validator:
    def __init__(self, rule_book, validation_error, game_state, role):
        self._rule_book = rule_book
        self._validationError = validation_error
        self._gameState = game_state
        self._role = role

    @property
    def validation_error(self):
        return self._validationError

    @property
    def rule_book(self):
        return self._rule_book

    # Validation for whether the stones are in the set intervall or whether the entered value is a digit
    def check_stone_input(self, input_strings, min_number, max_number):
        for element in input_strings:
            if not element.isdigit():
                raise self._validationError(f"Eingabe muss eine Ganzzahl zwischen {min_number} und {max_number} sein!")

            if int(element) < int(min_number) or int(element) > int(max_number):
                raise self._validationError(f"Eingabe muss eine Ganzzahl zwischen {min_number} und {max_number} sein!")

        return True

    # Validation for code length and whether the stones are in the set intervall or whether the entered value is a digit
    def check_code_input(self, input_strings, code_max_length, max_number):

        if len(input_strings) == code_max_length:
            return self.check_stone_input(input_strings, self._rule_book().min_check_code, int(max_number))
        else:
            raise self._validationError(f"Eingabe muss eine Länge von genau {code_max_length} haben!")

    def check_feedback_input(self, input_strings, code_max_length):
        if code_max_length >= len(input_strings) >= 0:
            if not input_strings:
                return True
            else:
                return self.check_stone_input(input_strings, self._rule_book().min_feedback_colour,
                                              self._rule_book().max_feedback_colour)
        else:
            raise self._validationError(f"Eingabe darf maximal eine Länge von {code_max_length} haben!")

    def set_digit_range(self, value, min_value, max_value):
        if value.isdigit():
            if min_value <= int(value) <= int(max_value):
                return True
            else:
                raise self._validationError(f"Eingabe muss eine Ganzzahl zwischen {min_value} und {max_value} sein!")
        else:
            raise self._validationError(f"Eingabe muss eine Ganzzahl zwischen {min_value} und {max_value} sein!")

    def check_max_code_length_input(self, code_max_length):
        return self.set_digit_range(code_max_length, self._rule_book().min_code_length, self._rule_book().max_code_length)

    # checks for game mode and depending on input for network and human or npc
    def check_game_mode_input(self, game_mode):
        return self.set_digit_range(game_mode, self._rule_book().min_game_mode, self._rule_book().max_game_mode)

    def check_max_colour_input(self, max_colour):
        return self.set_digit_range(max_colour, self._rule_book().min_colour, self._rule_book().max_colour)

    def check_game_state(self, board, user_role):
        winning_feedback_5 = board.convert_stone_array_to_colour(
            board.create_board_stone_array(self._rule_book().winning_feedback_5))
        winning_feedback_4 = board.convert_stone_array_to_colour(
            board.create_board_stone_array(self._rule_book().winning_feedback_4))
        board_feedback = board.convert_stone_array_to_colour(
            board.feedback)

        lose_condition_coder = user_role == self._role.Coder and (
                (winning_feedback_5 == board_feedback and len(winning_feedback_5) == len(board_feedback)) or
                (winning_feedback_4 == board_feedback and len(winning_feedback_4) == len(board_feedback))
        )

        win_condition_rater = user_role == self._role.Rater and (
                (winning_feedback_5 == board_feedback and len(winning_feedback_5) == board.code_max_length) or
                (winning_feedback_4 == board_feedback and len(winning_feedback_4) == board.code_max_length)
        )

        max_attempts_exceeded = board.attempt_counter > self._rule_book().max_try

        if user_role == self._role.Coder:
            return self._gameState.Win.value if not lose_condition_coder and max_attempts_exceeded else (
                self._gameState.Lose.value if lose_condition_coder else self._gameState.Undecided.value)
        elif user_role == self._role.Rater:
            return self._gameState.Win.value if win_condition_rater else (
                self._gameState.Lose.value if max_attempts_exceeded else self._gameState.Undecided.value)

    def check_port_input(self, input_string):
        for element in input_string:
            if not element.isdigit():
                raise self._validationError(f"Eingabe muss eine Ganzzahl sein!")

        return True
