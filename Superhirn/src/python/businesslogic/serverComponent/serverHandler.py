import socket

import requests


class ServerHandler:
    def __init__(self, ip, port, board, user_name):
        self._ip = ip
        self._port = port
        self._board = board
        self._user_name = user_name
        self._game_id = 0
        self._first_call_made = False
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._ip, int(self._port)))

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, game_id_input):
        self._game_id = game_id_input

    def convert_guess_to_string(self):
        if self._board.guessed_code:
            return ''.join([str(stone.colour.value) for stone in self._board.guessed_code])
        return ''

    def server_handler_send_json(self):
        move_data = {
            "gameid": self._game_id,
            "gamerid": self._user_name,
            "positions": self._board.code_max_length,
            "colors": self._board.max_colour,
            "value": self.convert_guess_to_string()
        }

        url = f'http://{self._ip}:{self._port}'
        headers = {'Content-Type': 'application/json'}
        return requests.post(url, json=move_data, headers=headers)

    def handle_response(self, response):
        if response.status_code == 404:
            print("Etwas is schief gelaufen: ", response.status_code)
        else:
            data = response.json()
            self.game_id = data["gameid"]
            if self._first_call_made:
                self._board.feedback = data["value"]
            else:
                self._first_call_made = True
