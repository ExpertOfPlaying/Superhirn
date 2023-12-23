from src.main.python.businesslogic.ruleBookComponent.ruleBook import *
from src.main.python.businesslogic.ruleBookComponent.validationError import ValidationError
from src.main.python.entities.userComponent.user import User
from src.main.python.presentation.terminal import *
from src.main.python.entities.boardComponent.board import Board


def user_help():
    print("Colour-Coding: RED = 1 GREEN = 2 YELLOW = 3 BLUE = 4 ORANGE = 5 BROWN = 6 WHITE = 7 BLACK = 8")
    print("Reset the game: r")
    print("Quit the game: q")


def reset():
    pass


def quit_game():
    pass


def setup_game():
    code_max_length = ""
    max_colour = ""
    attempt_counter = 0
    guessed_code = ""
    code = ""
    feedback = ""
    game_mode = ""
    user_name = ""

    # choose game_mode
    view_game_mode()
    mode = False
    while not mode:
        try:
            game_mode = input()
            mode = check_game_mode_input(game_mode)
        except ValidationError as error:
            print(error)

    # choose user_name
    view_user_name()
    user_name = input()

    # choose code_max_length
    view_code_length()
    length = False
    while not length:
        try:
            code_max_length = input()
            length = check_game_mode_input(code_max_length)
        except ValidationError as error:
            print(error)

    # choose max_colour
    view_max_colour()
    colour = False
    while not colour:
        try:
            max_colour = input()
            colour = check_game_mode_input(max_colour)
        except ValidationError as error:
            print(error)

    user = User(game_mode, user_name)
    board = Board(code_max_length, max_colour, attempt_counter, guessed_code, code, feedback, game_mode)
    return user, board
