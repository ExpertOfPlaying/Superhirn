from .validationError import ValidationError


def check_stone_input(input_string, min_number, max_number):
    if input_string.isdigit():
        stones = [int(num) for num in input_string]
        for stone in stones:
            if stone < int(min_number) or stone > int(max_number):
                raise ValidationError(f"Input must be integers between {min_number} and {max_number}!")
        return True
    else:
        raise ValidationError(f"Input must be integers between {min_number} and {max_number}!")


def set_digit_range(value, min_value, max_value):
    if value.isdigit():
        if min_value <= int(value) <= max_value:
            return True
        else:
            raise ValidationError(f"Input must be an integer between {min_value} or {max_value}!")
    else:
        raise ValidationError(f"Input must be an integer between {min_value} or {max_value}!")


def check_win(guess, code):
    if guess == code:
        return True
    else:
        return False


class RuleBook:
    min_check_code = 1
    min_code_length = 4
    max_code_length = 5
    min_game_mode = 1
    max_game_mode = 2
    min_colour = 2
    max_colour = 8
    max_try = 10
    min_feedback_colour = 7
    max_feedback_colour = 8

    # Validation for whether the stones are in the set intervall or whether the entered value is a digit

    # Validation for code length and whether the stones are in the set intervall or whether the entered value is a digit
    def check_code_input(self, input_string, code_max_length, max_number):
        if len(input_string) == code_max_length:
            return check_stone_input(input_string, self.min_check_code, int(max_number))
        else:
            raise ValidationError(f"Input must be equal to {code_max_length}!")

    def check_feedback_input(self, input_string, code_max_length):
        if code_max_length >= len(input_string) > 0:
            if input_string == "":
                return True
            else:
                return check_stone_input(input_string, self.min_feedback_colour, self.max_feedback_colour)
        else:
            raise ValidationError(f"Input must be equal or less to {code_max_length}!")

    def check_max_code_length_input(self, code_max_length):
        return set_digit_range(code_max_length, self.min_code_length, self.max_code_length)

    def check_game_mode_input(self, game_mode):
        return set_digit_range(game_mode, self.min_game_mode, self.max_game_mode)

    def check_max_colour_input(self, max_colour):
        return set_digit_range(max_colour, self.min_colour, max_colour)

    def check_lose(self, actual_attempt):
        if actual_attempt > self.max_try:
            return True
        else:
            return False
