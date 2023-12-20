from validationError import ValidationError


def check_stone_input(self, input_string):
    stones = [int(num) for num in input_string]
    for stone in stones:
        if stone < 2 or stone > 8:
            raise ValidationError("Input must be between 2 and 8")
        else:
            return True


def check_input_int_only(self, input_string):
    pass


def check_code_input(self):
    pass


def check_feedback_input(self):
    pass


def check_guessed_code_input(self):
    pass


def check_code_max_length_input(self):
    pass


def check_game_mode_input(self):
    pass


class RuleBook:
    def __init__(self, secret_code):
        self.secret_code = secret_code

    def check_win(self, guess):
        pass

    def check_feedback(self, guess):
        pass
