import os
from src.main.python.businesslogic.ruleBookComponent.ruleBook import *


class TerminalView:
    # input() schon fertig
    # print() schon fertig
    newline = os.linesep

    def game_mode(self):
        message = f"Welcome to the Superhirn {self.newline}"
        message += f"Please choose game-mode:{self.newline}"
        message += f"1. Coder{self.newline}"
        message += f"2. Rater{self.newline}"
        print(message)

    def game_network_mode(self):
        message = f"Please choose network mode:{self.newline}"
        message += f"1. Local{self.newline}"
        message += f"2. Online{self.newline}"
        print(message)

    def human_or_npc(self):
        message = f"Is Rater human or npc?{self.newline}"
        message += f"1. human{self.newline}"
        message += f"2. npc{self.newline}"
        print(message)

    def code_length(self):
        message = f"Please choose code_length between {min_code_length} and {max_code_length}."
        print(message)

    def max_colour(self):
        message = f"Please chose max_colour between {min_colour} and {max_colour}."
        print(message)

    def username(self):
        message = f"Please choose a username."
        print(message)

    def provide_guess(self):
        message = "Please provide a guess"
        print(message)

    def provide_code(self):
        message = f"Please provide a code"
        print(message)

    def win(self):
        message = f"You have won!"
        print(message)

    def lose(self):
        message = f"You have lost!"
        print(message)
