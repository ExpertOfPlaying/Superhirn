from src.main.python.businesslogic.ruleBookComponent.ruleBook import *
from src.main.python.businesslogic.ruleBookComponent.validationError import ValidationError


def coder_game():
    while True:
        try:
            print("Enter the code length for this game!")
            code_length = input()
            check_max_code_length_input(code_length)
        except ValidationError as error:
            print(error)
