from src.main.python.businesslogic.ruleBookComponent.ruleBook import *
from src.main.python.businesslogic.ruleBookComponent.validationError import ValidationError
from src.main.python.presentation.terminal import *
from src.main.python.entities.boardComponent.board import Board


def coder_game():
    while True:
        try:
            print("Enter the code length for this game!")
            check_max_code_length_input(input())
        except ValidationError as error:
            print(error)
