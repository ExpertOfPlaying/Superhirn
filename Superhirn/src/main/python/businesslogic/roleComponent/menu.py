from src.main.python.entities.userComponent.user import User
from src.main.python.entities.boardComponent.board import Board
# from .coder import coder_game
from .rater import guesser_game


def user_help():
    pass


def reset():
    pass


def quit_game():
    pass


class Menu:
    def __init__(self, validator, terminal):
        self.validator = validator
        self.terminal = terminal
        self.guesser = False
        self.coder = False

    def setup_game(self):
        code_max_length = ""
        max_colour = ""
        attempt_counter = 0
        guessed_code = ""
        code = ""
        feedback = ""
        game_mode = ""
        user_name = ""
        user = User(game_mode, user_name)

        # choose game_mode
        self.terminal.view_game_mode()
        mode = False
        while not mode:
            try:
                game_mode = input()
                mode = self.validator.check_game_mode_input(game_mode)
                user.role = game_mode
                if user.role == user.role.Coder:
                    self.coder = mode
                if user.role == user.role.Rater:
                    self.guesser = mode
            except self.validator.validationError as error:
                print(error)

        # choose user_name
        self.terminal.view_username()
        user.name = input()

        # choose code_max_length
        self.terminal.view_code_length()
        length = False
        while not length:
            try:
                code_max_length = input()
                length = self.validator.check_max_code_length_input(code_max_length)
            except self.validator.validationError as error:
                print(error)

        # choose max_colour
        self.terminal.view_max_colour()
        colour = False
        while not colour:
            try:
                max_colour = input()
                colour = self.validator.check_max_colour_input(max_colour)
            except self.validator.validationError as error:
                print(error)

        board = Board(code_max_length, max_colour, attempt_counter, guessed_code, code, feedback, game_mode)

        if self.guesser:
            guesser_game(user, board)
        if self.coder:
            self.coder_game(user, board)

    def coder_game(self, user, board):
        self.terminal.view_provide_code()
        code = False
        while not code:
            try:
                board.code = input()
                code = self.validator.check_code_input(board.code, board.code_max_length, board.max_colour)
            except self.validator.validationError as error:
                print(error)

        end = False
        while not end:
            try:
                # npc(user.role, board.code)
                self.terminal.view_provide_feedback()
                board.feedback = input()
                self.validator.check_feedback_input(board.feedback, board.code_max_length)
                board.attempt_counter = board.attempt_counter + 1
                if board.attempt_counter == board.max_attempts:
                    self.terminal.view_win()
                    end = True
            except self.validator.validationError as error:
                print(error)
