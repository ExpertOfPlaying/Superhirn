import json
import socket

import requests


class ServerHandler:
    def __init__(self, ip, port, board, user_name):
        self._ip = ip
        self._port = port
        self._board = board
        self._user_name = user_name
        self._game_id = 0
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._ip, int(self._port)))

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, game_id_input):
        self._game_id = game_id_input

    # Data The ID of a certain game. 0 if you want to start a new game. Get a ID as response that we need to use
    # after that.
    # game_id = 0
    # The ID (String) of the gamer. Freely selectable at the beginning of the game.
    # gamer_id = self._user_name
    # How many positions (>=1, <=9) does the pattern to be guessed have?. Selectable at the beginning of
    # the game.
    # positions = self._board.code_max_length
    # What is the maximum number of different colors (>=1, <=8) in the pattern to be guessed?. Selectable at
    # the beginning of the game.
    # colors = self._board.max_colour
    # Either the attempt to be evaluated (request to the server) or the evaluation (response from the
    # server). Empty String at game start.
    # value = ""

    def server_handler_send_json(self):
        # JSON für den POST-Request erstelle
        # "$schema": "https://json-schema.org/draft/2020-12/schema",
        # "$id": "https://htwberlin.com/ssr/superhirnserver/move_schema.json",
        # "title": "Move",
        # "_comment": "Farbkodierung= 1=Rot, 2=Grün, 3=Gelb, 4=Blau, 5=Orange, 6=Braun, 7=Weiss (Bewertung bzw.
        # Spielfarbe), 8=Schwarz (Bewertung bzw. Spielfarbe)",
        # "required": ["gameid", "gamerid", "positions", "colors", "value"]
        move_data = {
            "gameid": int(self._game_id),
            "gamerid": self._user_name,
            "positions": int(self._board.code_max_length),
            "colors": int(self._board.max_colour),
            "value": self._board.guessed_code
        }

        # JSON in String umwandeln
        json_data = json.dumps(move_data)

        # POST-Request senden mit Header
        url = f'http://{self._ip}:{self._port}'
        # headers = {'Content-Type': 'application/json'} wird automatisch durch json=json_data hinzugefügt
        return requests.post(url, json=json_data)

    def handle_response(self, response):
        # Antwort anzeigen
        global data
        if response.status_code == 200:
            content = response.content
            data = json.loads(content)
        if 'gameid' in data and data['gameid']:
            self.game_id = data['gameid']
        if "value" in data and data["value"]:
            self._board.feedback = data['value']
