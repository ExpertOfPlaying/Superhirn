from src.main.python.businesslogic.gameControllerComponent.gameController import *
from src.main.python.entities.userComponent import roleEnum


def main():
    setup_game()
    if setup_game().board.game_mode == roleEnum.Role.Coder:
        coder_game()
    if setup_game().board.game_mode == roleEnum.Role.Rater:
        guesser_game()


if __name__ == "__main__":
    main()
