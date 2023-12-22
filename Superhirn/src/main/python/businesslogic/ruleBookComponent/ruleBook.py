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


# Validation for code length and whether the stones are in the set intervall or whether the entered value is a digit
def check_code_input(input_string, code_max_length, max_number):
    if len(input_string) == code_max_length:
        return check_stone_input(input_string, 1, int(max_number))
    else:
        raise ValidationError(f"Input must be equal to {code_max_length}!")


def check_feedback_input(input_string, code_max_length):
    if code_max_length >= len(input_string) > 0:
        if input_string == "":
            return True
        else:
            return check_stone_input(input_string, 7, 8)
    else:
        raise ValidationError(f"Input must be equal or less to {code_max_length}!")


def set_digit_range(value, min_value, max_value):
    if value.isdigit():
        if min_value <= int(value) <= max_value:
            return True
        else:
            raise ValidationError(f"Input must be an integer between {min_value} or {max_value}!")
    else:
        raise ValidationError(f"Input must be an integer between {min_value} or {max_value}!")


def check_max_code_length_input(code_max_length):
    return set_digit_range(code_max_length, 4, 5)


def check_game_mode_input(game_mode):
    return set_digit_range(game_mode, 1, 2)


def check_max_colour_input(max_colour):
    return set_digit_range(max_colour, 2, 8)


def check_win(guess, code):
    if guess == code:
        return True
    else:
        return False


def check_lose(max_counter):
    if max_counter > 10:
        return True
    else:
        return False
