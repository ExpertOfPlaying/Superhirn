from src.main.python.entities.userComponent.user import User
from src.main.python.entities.boardComponent.board import Board
from src.main.python.businesslogic.npcComponent.npc import NPC


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

    def setup_game(self):
        code_max_length = ""
        max_colour = ""
        attempt_counter = 1
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
        npc = NPC(board)

        if user.role == user.role.Rater:
            self.guesser_game(user.role, npc, board)
        if user.role == user.role.Coder:
            self.coder_game(user.role, npc, board)

    def coder_game(self, role, npc, board):
        self.terminal.view_provide_code()
        code = False
        while not code:
            try:
                code_input = input()
                code = self.validator.check_code_input(code_input, board.code_max_length, board.max_colour)
                board.code = code_input
            except self.validator.validationError as error:
                print(error)

        end = False
        while not end:
            try:
                # npc(user.role) returns guess
                board.guessed_code = "12345"
                self.terminal.view_draw(board, role)
                while True:
                    try:
                        self.terminal.view_provide_feedback()
                        feedback_input = input()
                        self.validator.check_feedback_input(feedback_input, board.code_max_length)
                        board.feedback = feedback_input
                        board.attempt_counter = board.attempt_counter + 1
                        if board.attempt_counter == board.max_attempts:
                            self.terminal.view_win()
                            end = True
                            break
                        else:
                            break
                    except self.validator.validationError as error:
                        print(error)
            except self.validator.validationError as error:
                print(error)

    def guesser_game(self, role, npc, board):
        end = False
        npc.generate_code()

        while not end:
            try:
                self.terminal.view_draw(board, npc.role)

                self.terminal.view_provide_guess()
                guess_input = input()

                self.validator.check_code_input(guess_input, board.code_max_length, board.max_colour)
                board.guessed_code = guess_input
                board.attempt_counter = board.attempt_counter + 1
                npc.generate_feedback()

                if not self.validator.check_game_state(board, role):
                    self.terminal.view_lose()
                    end = True
                    break
                elif self.validator.check_game_state(board, role) == True:
                    print(self.validator.check_game_state(board, role))
                    self.terminal.view_win()
                    end = True
                    break

            except self.validator.validationError as error:
                print(error)

        self.terminal.view_draw(board, role)
