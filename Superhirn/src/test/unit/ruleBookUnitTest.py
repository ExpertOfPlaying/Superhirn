import unittest
from src.main.python.businesslogic.ruleBookComponent.ruleBook import *
from src.main.python.businesslogic.ruleBookComponent.validationError import ValidationError
from src.main.python.entities.boardComponent.board import Board


class TestRuleBookClass(unittest.TestCase):
    def setUp(self):
        # Set up a RuleBook instance with a secret code
        self.secret_code = "12345"

        # code length
        self.good_max_code_length_input_string = "5"
        self.bad_high_max_code_length_input_string = "6"
        self.bad_low_max_code_length_input_string = "3"
        self.bad_char_code_length_input_string = "a"

        # code or guess input
        self.good_stone_input_string = "12345"
        self.bad_out_of_bounds_stone_input_string = "12348"
        self.bad_high_stone_input_string = "123456"
        self.bad_low_stone_input_string = "123"
        self.bad_char_stone_input_string = "abcde"

        # amount colours per game
        self.good_max_code_colours = "7"
        self.bad_max_low_code_colours = "1"
        self.bad_max_high_code_colours = "9"
        self.bad_char_code_colours = "a"

        # feedback input
        self.good_feedback_input_string = "78"
        self.good_feedback_input_string_win = "88888"
        self.good_no_feedback_input_string = ""
        self.bad_high_feedback_input_string = "777777"
        self.bad_out_of_bounds_feedback_input_string = "12345"
        self.bad_char_feedback_input_string = "abcde"

        # game-mode
        self.good_game_mode_coder = "1"
        self.good_game_mode_guesser = "2"
        self.bad_multiple_game_mode_input = "12"
        self.bad_singular_game_mode_input = "3"
        self.bad_char_game_mode_input = "a"

        # Board
        self.board = Board(self.good_max_code_length_input_string, self.good_max_code_colours, 1,
                           self.good_stone_input_string, self.secret_code,
                           self.good_feedback_input_string_win, self.good_game_mode_guesser)

    # check_win
    def test_check_win_correct_guess(self):
        self.assertTrue(check_win(self.board.guessed_code, self.board.code))

    def test_check_win_incorrect_guess(self):
        self.assertFalse(check_win(self.bad_out_of_bounds_stone_input_string, self.board.code))

    # check_lose
    def test_check_lose(self):
        self.board.attempt_counter = 11
        self.assertTrue(check_lose(self.board.attempt_counter))

    # check_stone_input
    def test_check_stone_input_good(self):
        self.assertTrue(check_stone_input(self.good_stone_input_string, 1, self.board.max_colour))

    def test_check_stone_input_bad_out_of_bounds(self):
        with self.assertRaises(ValidationError) as exception:
            check_stone_input(self.bad_out_of_bounds_stone_input_string, 1, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    def test_check_stone_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_stone_input(self.bad_char_stone_input_string, 1, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    # check_code_input
    def test_check_code_input_good(self):
        self.assertTrue(check_code_input(
            self.good_stone_input_string, self.board.code_max_length, self.board.max_colour))

    def test_check_code_input_bad_length_high(self):
        with self.assertRaises(ValidationError) as exception:
            check_code_input(self.bad_high_stone_input_string, self.board.code_max_length, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    def test_check_code_input_bad_length_low(self):
        with self.assertRaises(ValidationError) as exception:
            check_code_input(self.bad_low_stone_input_string, self.board.code_max_length, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    def test_check_code_input_bad_out_of_bounds(self):
        with self.assertRaises(ValidationError) as exception:
            check_code_input(
                self.bad_out_of_bounds_stone_input_string, self.board.code_max_length, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    def test_check_code_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_stone_input(self.bad_char_stone_input_string, 1, self.board.max_colour)
        exception_message = exception.exception
        print(exception_message)

    # check_feedback_input
    def test_check_feedback_input_good(self):
        self.assertTrue(check_feedback_input(self.good_feedback_input_string, self.board.code_max_length))

    def test_check_feedback_input_bad_high(self):
        with self.assertRaises(ValidationError) as exception:
            check_feedback_input(
                self.bad_high_feedback_input_string, self.board.code_max_length)
        exception_message = exception.exception
        print(exception_message)

    def test_check_feedback_input_bad_out_of_bounds(self):
        with self.assertRaises(ValidationError) as exception:
            check_feedback_input(
                self.bad_out_of_bounds_feedback_input_string, self.board.code_max_length)
        exception_message = exception.exception
        print(exception_message)

    def test_check_feedback_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_feedback_input(
                self.bad_char_feedback_input_string, self.board.code_max_length)
        exception_message = exception.exception
        print(exception_message)

    def test_check_max_code_length_input_good(self):
        self.assertTrue(check_max_code_length_input(self.good_max_code_length_input_string))

    def test_check_max_code_length_input_bad_high(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_code_length_input(self.bad_high_max_code_length_input_string)
        exception_message = exception.exception
        print(exception_message)

    def test_check_max_code_length_input_bad_low(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_code_length_input(self.bad_low_max_code_length_input_string)
        exception_message = exception.exception
        print(exception_message)

    def test_check_max_code_length_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_code_length_input(self.bad_char_code_length_input_string)
        exception_message = exception.exception
        print(exception_message)

    # check_game_mode
    def test_check_game_mode_input_good(self):
        self.assertTrue(check_game_mode_input(self.good_game_mode_coder))

    def test_check_game_mode_input_bad_singular(self):
        with self.assertRaises(ValidationError) as exception:
            check_game_mode_input(self.bad_singular_game_mode_input)
        exception_message = exception.exception
        print(exception_message)

    def test_check_game_mode_input_bad_multiple(self):
        with self.assertRaises(ValidationError) as exception:
            check_game_mode_input(self.bad_multiple_game_mode_input)
        exception_message = exception.exception
        print(exception_message)

    def test_check_game_mode_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_code_length_input(self.bad_char_game_mode_input)
        exception_message = exception.exception
        print(exception_message)

    # check_max_colour_input
    def test_check_max_colour_input_good(self):
        self.assertTrue(check_max_colour_input(self.good_max_code_colours))

    def test_check_max_colour_input_bad_high(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_colour_input(self.bad_max_high_code_colours)
        exception_message = exception.exception
        print(exception_message)

    def test_check_max_colour_input_bad_low(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_colour_input(self.bad_max_low_code_colours)
        exception_message = exception.exception
        print(exception_message)

    def test_check_max_colour_input_bad_char(self):
        with self.assertRaises(ValidationError) as exception:
            check_max_colour_input(self.bad_char_code_colours)
        exception_message = exception.exception
        print(exception_message)


if __name__ == "__main__":
    unittest.main()
