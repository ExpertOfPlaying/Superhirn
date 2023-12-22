from .validationError import ValidationError


# Validation for whether the stones are in the set intervall or whether the entered value is a digit
def check_stone_input(input_string, min_number, max_number):
    if input_string.isdigit():
        stones = [int(num) for num in input_string]
        for stone in stones:
            if stone < int(min_number) or stone > int(max_number):
                raise ValidationError(f"Input must be integers between {min_number} and {max_number}!")
        return True
    else:
        raise ValidationError(f"Input must be integers between {min_number} and {max_number}!")


def check_code_input(input_string, actual_board, max_number):  # coder gibt ein 12345 oder 1234
    if len(input_string) == actual_board.code_max_length:
        check_stone_input(input_string, 2, max_number)
    else:
        raise ValidationError(f"Input must be equal to {actual_board.code_max_length}!")


def check_feedback_input(input_string, actual_board):
    if len(input_string) <= actual_board.code_max_length or len(input_string) > 0:
        if input_string == "":
            return True
        else:
            check_stone_input(input_string, 7, 8)
    else:
        raise ValidationError(f"Input must be equal or less to {actual_board.code_max_length}!")


def check_max_code_length_input():
    pass


def check_game_mode_input():
    pass


def check_max_colour_input():
    pass


class RuleBook:
    def __init__(self, secret_code):
        self.secret_code = secret_code

    def check_win(self, guess):
        pass

    def check_feedback(self, guess):
        pass
