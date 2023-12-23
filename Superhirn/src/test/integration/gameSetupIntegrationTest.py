import unittest
from src.main.python.businesslogic.roleComponent.role import *


class GameSetupIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.board = (
            Board("5", "7", 1, "", "", "", "1"))

    def test_game_setup(self):
        setup_board = setup_game()
        self.assertEqual(self.board.game_mode, setup_board.game_mode)


if __name__ == '__main__':
    unittest.main()
