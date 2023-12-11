import unittest
from unittest.mock import Mock, patch

from src.main.python.entities.boardComponent.board import Board
from src.main.python.businesslogic.roleComponent.rater import Rater


class TestBoardClass(unittest.TestCase):

    def setUp(self):
        self.test_board = Board(5, 10)

    # get set value for guesses

    def test_get_guess_attempts(self):
        self.assertEqual(self.test_board.attempts, 10)

    def test_get_guess_attempts_exception_under(self):
        with self.assertRaises(ValueError) as exception:
            self.test_board.attempts = 0
        exception_message = exception.exception
        print(exception_message)

    def test_get_guess_attempts_exception_over(self):
        with self.assertRaises(ValueError) as exception:
            self.test_board.attempts = 11
        exception_message = exception.exception
        print(exception_message)

    def test_get_guess_attempts_exception_none(self):
        with self.assertRaises(TypeError) as exception:
            self.test_board.attempts = None
        exception_message = exception.exception
        print(exception_message)

    def test_get_guess_attempts_exception_empty(self):
        with self.assertRaises(TypeError) as exception:
            test_board = Board(5, )
        exception_message = exception.exception
        print(exception_message)

    def test_get_guess_attempts_exception_not_int(self):
        with self.assertRaises(TypeError) as exception:
            self.test_board.attempts = "b"
        exception_message = exception.exception
        print(exception_message)

    # get set code length for the game

    def test_set_get_code_length(self):
        self.assertEqual(self.test_board.code_length, 5)

    def test_set_get_code_length_exception_under(self):
        with self.assertRaises(ValueError) as exception:
            self.test_board.code_length = 3
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_code_length_exception_over(self):
        with self.assertRaises(ValueError) as exception:
            self.test_board.code_length = 6
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_code_length_exception_none(self):
        with self.assertRaises(TypeError) as exception:
            self.test_board.code_length = None
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_code_length_exception_empty(self):
        empty = ''
        with self.assertRaises(TypeError) as exception:
            test_board = Board(empty, 10)
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_code_length_exception_not_int(self):
        with self.assertRaises(TypeError) as exception:
            self.test_board.code_length = "b"
        exception_message = exception.exception
        print(exception_message)

    # get set code array

    def test_set_get_code(self):
        rater = Rater()
        with patch.object(rater, 'add_guess', return_value=None):
            result = self.test_board.code()

    # get set guess arrays

    def test_set_get_guess_list_one(self):
        rater = Rater()
        rater.add_guess()
        array_of_guesses[expected_guess, expected_guess, expected_guess]

        expected_guess = [1, 2, 3, 4, 5]

        board.get_guess_list()
        x = guesslist[0]

        board.guesslist[guess1,guess2]
        len(expected_guess)
        self.assertEqual(board.guesslist(get_array_lenght()-1), expected_guess)

    def test_set_get_guess_exception_under(self):
        board.set_guess(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError) as exception:
            board.get_guess(get_array_length()-2)
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_guess_exception_over(self):
        board.set_guess(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError) as exception:
            board.get_guess(get_array_length()+2)
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_guess_exception_empty(self):
        board.set_guess(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError) as exception:
            board.get_guess()
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_guess_exception_none(self):
        board.set_guess(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError) as exception:
            board.get_guess(None)
        exception_message = exception.exception
        print(exception_message)

    def test_set_get_guess_exception_no_array(self):
        with self.assertRaises(ValueError) as exception:
            board.get_guess(1)
        exception_message = exception.exception
        print(exception_message)

    # get set feedback

    def test_get_feedback(self):
        board.set_feedback(7, 7, 8)
        expected_feedback = [7, 7, 8]
        self.assertEqual(board.get_feedback(), expected_feedback)


if __name__ == '__main__':
    unittest.main()
