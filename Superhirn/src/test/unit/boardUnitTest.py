import unittest
from unittest.mock import MagicMock
from src.main.python.entities.boardComponent.board import Board
from src.main.python.entities.stoneComponent.stone import Stone
from numpy.testing import assert_array_equal


class TestBoardClass(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 0, [], [], [], "")

    def test_create_board(self):
        self.assertTrue(isinstance(self.board, Board))

    def test_create_board_with_correct_code_max_length(self):
        self.assertEqual(self.board.code_max_length, 5)

    def test_create_board_with_correct_attempt_counter(self):
        self.assertEqual(self.board.attempt_counter, 0)

    def test_create_board_with_correct_guessed_code(self):
        self.assertEqual(self.board.guessed_code, [])

    def test_create_board_with_correct_code(self):
        self.assertEqual(self.board.code, [])

    def test_create_board_with_correct_feedback(self):
        self.assertEqual(self.board.feedback, [])

    def test_create_board_with_correct_game_mode(self):
        self.assertEqual(self.board.game_mode, "")

    def test_set_max_attempt(self):
        self.board.max_attempt = 20
        self.assertEqual(self.board.max_attempt, 20)

    def test_set_attempt_counter(self):
        self.board.attempt_counter = 10
        self.assertEqual(self.board.attempt_counter, 10)

    def test_set_guessed_code(self):
        user_input1 = "12345"
        self.board.guessed_code = [int(num) for num in user_input1]
        value_list = []
        for stone in self.board.guessed_code:
            value_list.append(stone.colour)
        board_stone = [Stone(1).colour, Stone(2).colour, Stone(3).colour, Stone(4).colour, Stone(5).colour]
        self.assertEqual(board_stone, value_list)

    def test_get_guessed_code_list(self):
        self.assertEqual(self.board.guessed_code_list, [])

    def test_add_guessed_code_list(self):
        user_input1 = "12345"
        self.board.guessed_code = [int(num) for num in user_input1]
        self.board.add_guessed_code_list()
        user_input2 = "54321"
        self.board.guessed_code = [int(num) for num in user_input2]
        self.board.add_guessed_code_list()
        self.assertEqual(len(self.board.guessed_code_list), 2)

    def test_get_code(self):
        self.assertEqual(self.board.code, [])

    def test_set_code(self):
        user_input = "12345"
        self.board.code = [int(num) for num in user_input]
        value_list = []
        for stone in self.board.code:
            value_list.append(stone.colour)
        board_stone = [Stone(1).colour, Stone(2).colour, Stone(3).colour, Stone(4).colour, Stone(5).colour]
        self.assertEqual(board_stone, value_list)

    def test_get_feedback(self):
        self.assertEqual(self.board.feedback, [])

    def test_set_feedback(self):
        user_input = "12345"
        self.board.feedback = [int(num) for num in user_input]
        value_list = []
        for stone in self.board.feedback:
            value_list.append(stone.colour)
        board_stone = [Stone(1).colour, Stone(2).colour, Stone(3).colour, Stone(4).colour, Stone(5).colour]
        self.assertEqual(board_stone, value_list)

    def test_get_game_mode(self):
        self.assertEqual(self.board.game_mode, "")

    def test_feedback_list(self):
        self.assertEqual(self.board.feedback_list, [])

    def test_set_feedback_list(self):
        user_input1 = "12345"
        self.board.feedback = [int(num) for num in user_input1]
        self.board.add_feedback_list()
        user_input2 = "54321"
        self.board.feedback = [int(num) for num in user_input2]
        self.board.add_feedback_list()
        self.assertEqual(2, len(self.board.feedback_list))


if __name__ == '__main__':
    unittest.main()
