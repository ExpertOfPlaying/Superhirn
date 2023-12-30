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
        message = f"Willkommen  zu Super Superhirn {os.linesep}"
        message += f"Bitte wähle einen Spielmodus aus:{os.linesep}"
        message += f"1. Coder{os.linesep}"
        message += f"2. Rater{os.linesep}"
        print(message)

    @staticmethod
    def view_game_network_mode():
        message = f"Bitte wähle einen Netzwerkmodus aus:{os.linesep}"
        message += f"1. Local{os.linesep}"
        message += f"2. Online{os.linesep}"
        print(message)

    @staticmethod
    def view_human_or_npc():
        message = f"Soll der Rater menschlich sein oder ein NPC?{os.linesep}"
        message += f"1. menschlich{os.linesep}"
        message += f"2. NPC{os.linesep}"
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
        message = f"Bitte wähle die Codelänge zwischen {RuleBook().min_code_length} und {RuleBook().max_code_length}."
        print(message)

    @staticmethod
    def view_max_colour():
        message = f"Bitte wähle die maximale Farbenanzahl zwischen {RuleBook().min_colour} und {RuleBook().max_colour}."
        print(message)

    @staticmethod
    def view_username():
        message = f"Bitte wähle einen Benutzernamen."
        print(message)

    @staticmethod
    def view_provide_guess():
        message = "Bitte gib deinen Rateversuch ein."
        print(message)

    @staticmethod
    def view_provide_code():
        message = f"Bitte gib deinen Code ein."
        print(message)

    @staticmethod
    def view_provide_feedback():
        message = f"Bitte gib dein Feedback"
        print(message)

    @staticmethod
    def view_win():
        message = f"Du hast gewonnen!"
        print(message)

    @staticmethod
    def view_lose():
        message = f"Du hast verloren!"
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
        message = f"Colour-Coding: Rot = 1 Grün = 2 Gelb = 3 Blau = 4 Orange = 5 Braun = 6 Weiß = 7 Schwarz = 8{os.linesep}"
        message += f"Spiel zurücksetzen: r{os.linesep}"
        message += f"Spiel beenden: q{os.linesep}"
        print(message)
