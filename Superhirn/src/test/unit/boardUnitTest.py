import unittest
from unittest.mock import MagicMock
from src.main.python.entities.boardComponent.board import Board

class TestBoardClass(unittest.TestCase):

    def create_board_with_correct_parameters(self):
        board = Board()
        assert isinstance(board, Board)

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
