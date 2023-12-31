import sys

from src.python.entities.userComponent.user import User
from src.python.entities.boardComponent.board import Board
from src.python.businesslogic.npcComponent.npc import NPC
from src.python.businesslogic.serverComponent.serverHandler import ServerHandler


def command_checker(user_input, terminal, validator, npc_feedback_error, user_name):
    if user_input == "/q":
        quit_game()
    elif user_input == "/h":
        user_help(terminal)
    elif user_input == "/r":
        reset(validator, terminal, npc_feedback_error, user_name)


def user_help(view):
    view.print_help()


def reset(validator, terminal, npc_feedback_error, user_input):
    return GameController(validator, terminal, npc_feedback_error, user_input).setup_game()


def quit_game():
    sys.exit()


class GameController:
    def __init__(self, validator, terminal, npc_feedback_error, user_name=None):
        self._validator = validator
        self._terminal = terminal
        self._npc_feedback_error = npc_feedback_error
        self._user_name = user_name

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, name):
        self._user_name = name

    def setup_game(self):
        user = User("", self._user_name)
        self.choose_game_mode(user)

        network_mode = None
        network_config = None
        npc_rater = False
        if user.role == user.role.Rater:
            network_mode, network_config = self.setup_network_mode()
            if network_mode == "2":  # Online-Spiel
                npc_rater = self.choose_npc_rater()

        if not self._user_name:
            self.choose_user_name(user)
        code_max_length = self.choose_code_max_length()
        max_colours = self.choose_max_colour()
        self.initialize_game(network_mode, network_config, code_max_length, max_colours, user, npc_rater)

    def choose_game_mode(self, user):
        game_mode = self.get_user_input(self._terminal.view_game_mode, self._validator.check_game_mode_input)
        user.role = game_mode

    def setup_network_mode(self):
        network_mode = self.get_user_input(self._terminal.view_game_network_mode,
                                           self._validator.check_game_mode_input)

        if network_mode == "2":  # Online-Spiel
            ip = self.get_user_input(self._terminal.view_ip_address)
            port = self.get_user_input(self._terminal.view_port, self._validator.check_port_input)
            return network_mode, (ip, port)

        return network_mode, None

    def choose_npc_rater(self):
        choice = self.get_user_input(self._terminal.view_human_or_npc, self._validator.check_game_mode_input)
        return choice == "2"  # True, wenn NPC als Rater, False, wenn menschlicher Spieler

    def choose_user_name(self, user):
        user.name = self.get_user_input(self._terminal.view_username)
        self._user_name = user.name

    def choose_code_max_length(self):
        code_max_length = self.get_user_input(self._terminal.view_code_length,
                                              self._validator.check_max_code_length_input)
        return code_max_length

    def choose_max_colour(self):
        max_colour = self.get_user_input(self._terminal.view_max_colour,
                                         self._validator.check_max_colour_input)
        return max_colour

    def get_user_input(self, prompt, validation_function=None):
        valid_input = False
        while not valid_input:
            try:
                prompt()
                input_value = input()
                command_checker(input_value, self._terminal, self._validator, self._npc_feedback_error, self._user_name)
                if validation_function and not validation_function(input_value):
                    raise self._validator.validation_error("Ungültige Eingabe")

                return input_value
            except self._validator.validation_error as error:
                print(error)
        return valid_input

    def initialize_game(self, network_mode, network_config, code_max_length, max_colours, user, npc_rater):
        board = Board(code_max_length, max_colours, 1, "", "", "", user.role.value)
        npc = NPC(board)
        board.register_observer(npc)

        if network_mode == "2":
            ip, port = network_config
            server = ServerHandler(ip, port, board, user.name)
            self.guesser_game(user.role, npc, board, server, npc_rater)
        else:
            if user.role == user.role.Rater:
                self.guesser_game(user.role, npc, board)
            if user.role == user.role.Coder:
                self.coder_game(user.role, board)

    def coder_game(self, role, board):
        # Code zu Beginn des Spiels festlegen
        self.set_initial_code(board)

        while True:
            try:
                # NPC Rater soll einen Rateversuch machen
                board.notify_observers()
                self._terminal.view_draw(board, role)
                self.provide_feedback(board)

                if self.check_game_end(board, role):
                    self._terminal.view_draw(board, role)
                    reset(self._validator, self._terminal, self._npc_feedback_error, self._user_name)
            except self._npc_feedback_error as error:
                print(error)
                reset(self._validator, self._terminal, self._npc_feedback_error, self._user_name)

    def set_initial_code(self, board):
        code_input = self.get_valid_code_input(board, self._terminal.view_provide_code)
        board.code = code_input

    def get_valid_code_input(self, board, prompt):
        while True:
            try:
                prompt()
                code_input = input()
                command_checker(code_input, self._terminal, self._validator, self._npc_feedback_error, self._user_name)
                if self._validator.check_code_input(code_input, board.code_max_length, board.max_colour):
                    return code_input
            except self._validator.validation_error as error:
                print(error)

    def provide_feedback(self, board):
        self._terminal.view_provide_feedback()
        feedback_input = self.get_valid_feedback_input(board)
        board.feedback = feedback_input
        board.attempt_counter = board.attempt_counter + 1

    def get_valid_feedback_input(self, board):
        while True:
            try:
                feedback_input = input()
                command_checker(feedback_input, self._terminal, self._validator, self._npc_feedback_error, self._user_name)
                if self._validator.check_feedback_input(feedback_input, board.code_max_length):
                    return feedback_input
            except self._validator.validation_error as error:
                print(error)

    def guesser_game(self, role, npc, board, server=None, npc_rater=False):

        # NPC Coder soll einen Random Code erstellen oder Server soll das Spiel starten
        if server:
            self.start_online_game(server)
        else:
            board.notify_observers()

        while True:
            try:
                self._terminal.view_draw(board, role.Coder)
                self.perform_guesser_turn(npc, board, server, npc_rater, role)
                if not server:
                    # NPC Coder soll ein Feedback geben
                    board.notify_observers()

                if self.check_game_end(board, role):
                    self._terminal.view_draw(board, role)
                    reset(self._validator, self._terminal, self._npc_feedback_error, self._user_name)
            except self._npc_feedback_error as error:
                print(error)
                reset(self._validator, self._terminal, self._npc_feedback_error, self._user_name)

    @staticmethod
    def start_online_game(server):
        response = server.server_handler_send_json()
        server.handle_response(response)

    def perform_guesser_turn(self, npc, board, server, npc_rater, role):
        if npc_rater:
            try:
                npc.role = role.Rater
                self._terminal.view_provide_guess()
                # NPC soll einen Rateversuch machen
                board.notify_observers()
            except self._npc_feedback_error as error:
                print(error)
                reset(self._validator, self._terminal, self._npc_feedback_error, self._user_name)
        else:
            guess_input = self.get_valid_code_input(board, self._terminal.view_provide_guess)
            board.guessed_code = guess_input

        if server:
            response = server.server_handler_send_json()
            server.handle_response(response)

        board.attempt_counter = board.attempt_counter + 1

    def check_game_end(self, board, role):
        if not self._validator.check_game_state(board, role):
            self._terminal.view_lose()
            return True
        elif self._validator.check_game_state(board, role) == True:
            self._terminal.view_win()
            return True
        return False
