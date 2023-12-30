import os
from src.main.python.entities.ruleBookComponent.ruleBook import *


def background_colour(colour_value):
    if colour_value == 1:  # rot
        return "\x1b[41m\x1b[30m"  # Red background, black text
    elif colour_value == 2:  # grün
        return "\x1b[42m\x1b[30m"  # Green background, black text
    elif colour_value == 3:
        return "\x1b[44m\x1b[37m"  # Blue background, white text
    elif colour_value == 4:
        return "\x1b[43m\x1b[30m"  # Yellow background, black text
    elif colour_value == 5:
        return "\x1b[48;2;255;165;0m\x1b[30m"  # Orange background (RGB), black text
    elif colour_value == 6:  # sollte Braun sein
        return "\x1b[43m\x1b[30m"  # Yellow background, black text
    elif colour_value == 7:
        return "\x1b[47m\x1b[30m"  # White background, black text
    elif colour_value == 8:
        return "\x1b[40m\x1b[37m"  # Black background, white text


class TerminalView:
    # input() schon fertig
    # print() schon fertig

    @staticmethod
    def view_game_mode():
        message = f"Welcome to the Superhirn {os.linesep}"
        message += f"Please choose game-mode:{os.linesep}"
        message += f"1. Coder{os.linesep}"
        message += f"2. Rater{os.linesep}"
        print(message)

    @staticmethod
    def view_game_network_mode():
        message = f"Please choose network mode:{os.linesep}"
        message += f"1. Local{os.linesep}"
        message += f"2. Online{os.linesep}"
        print(message)

    @staticmethod
    def view_human_or_npc():
        message = f"Is Rater human or npc?{os.linesep}"
        message += f"1. human{os.linesep}"
        message += f"2. npc{os.linesep}"
        print(message)

    @staticmethod
    def view_ip_address():
        message = f"IP eingeben!{os.linesep}"
        print(message)

    @staticmethod
    def view_port():
        message = f"Port eingeben!{os.linesep}"
        print(message)

    @staticmethod
    def view_code_length():
        message = f"Please choose code_length between {RuleBook().min_code_length} and {RuleBook().max_code_length}."
        print(message)

    @staticmethod
    def view_max_colour():
        message = f"Please chose max_colour between {RuleBook().min_colour} and {RuleBook().max_colour}."
        print(message)

    @staticmethod
    def view_username():
        message = f"Please choose a username."
        print(message)

    @staticmethod
    def view_provide_guess():
        message = "Please provide a guess"
        print(message)

    @staticmethod
    def view_provide_code():
        message = f"Please provide a code"
        print(message)

    @staticmethod
    def view_provide_feedback():
        message = f"Please provide a feedback"
        print(message)

    @staticmethod
    def view_win():
        message = f"You have won!"
        print(message)

    @staticmethod
    def view_lose():
        message = f"You have lost!"
        print(message)

    @staticmethod
    def view_draw(actual_board, role):
        if actual_board.game_mode == role.value:
            if not actual_board.code:
                print("Code: Geheimer Server Code")
            else:
                print(f"Code:", end="")
                for stone in actual_board.code:
                    message = ""
                    message += background_colour(stone.colour.value)
                    message += f"[{stone.colour.value}]"
                    message += "\x1b[0m"  # Reset to the default color
                    print(message, end="")  # Print code without moving to the next line
                print()

        for i, (guessed_attempt, guessed_code) in enumerate(actual_board.guessed_code_list):
            print(f"{guessed_attempt}. Rateversuch:", end="")

            message = ""
            for stone in guessed_code:
                message += background_colour(stone.colour.value)
                message += f"[{stone.colour.value}]"
                message += "\x1b[0m"  # Reset to the default color
            print(message, end=" ")  # Print guess without moving to the next line

            # Print feedback if available
            if i < len(actual_board.feedback_list):
                feedback_attempt, feedback = actual_board.feedback_list[i]
                print(f"{i+1}. Feedback:", end="")

                message = ""
                for stone in feedback:
                    message += background_colour(stone.colour.value)
                    message += f"[{stone.colour.value}]"
                    message += "\x1b[0m"  # Reset to the default color
                print(message)  # Print feedback with a new line
            else:
                print()  # Print a new line if no feedback is available

    @staticmethod
    def print_help():
        message = f"Colour-Coding: RED = 1 GREEN = 2 YELLOW = 3 BLUE = 4 ORANGE = 5 BROWN = 6 WHITE = 7 BLACK = 8{os.linesep}"
        message += f"Reset the game: r{os.linesep}"
        message += f"Quit the game: q{os.linesep}"
        print(message)
