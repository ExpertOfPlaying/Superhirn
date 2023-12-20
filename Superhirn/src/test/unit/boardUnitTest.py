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
        userinput = "12345"
        self.board.guessed_code = [int(num) for num in userinput]
        value_list = []
        for stone in self.board.guessed_code:
            value_list.append(stone.colour)
        board_stone = [Stone(1).colour, Stone(2).colour, Stone(3).colour, Stone(4).colour, Stone(5).colour]
        self.assertEqual(value_list, board_stone)

    def test_get_guessed_code_list(self):
        self.assertEqual(self.board.guessed_code_list, [])

    def test_set_guessed_code_list(self):
        userinput1 = "12345"
        self.board.guessed_code1 = [int(num) for num in userinput1]
        self.board.add_guessed_code_list()
        userinput2 = "54321"
        self.board.guessed_code2 = [int(num) for num in userinput2]
        self.board.add_guessed_code_list()



    def make_new_valid_guess_as_int_array(self):
        pass

    def make_new_invalid_guess_as_int_array(self):
        pass

    def make_new_valid_guess_as_stone_array(self):
        pass

    def make_new_invalid_guess_as_stone_array(self):
        pass

    def define_valid_answer_code_as_string(self):
        pass

    def define_invalid_answer_code_as_string(self):
        pass


if __name__ == '__main__':
    unittest.main()
