import unittest
from src.main.python.businesslogic.ruleBookComponent.ruleBook import RuleBook, check_stone_input
from src.main.python.businesslogic.ruleBookComponent.validationError import ValidationError
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestRuleBookClass(unittest.TestCase):
    def setUp(self):
        # Set up a RuleBook instance with a secret code
        self.secret_code = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW, Colour.ORANGE]
        self.rule_book = RuleBook(self.secret_code)
        # code length
        self.good_max_code_length_input_string = "5"
        self.bad_max_high_code_length_input_string = "6"
        self.bad_max_low_code_length_input_string = "3"
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

    def test_check_win_correct_guess(self):
        # Test when the guess is correct
        correct_guess = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW, Colour.ORANGE]
        result = self.rule_book.check_win(correct_guess)
        self.assertTrue(result, "Expected checkWin to return True for a correct guess.")

    def test_check_win_incorrect_guess(self):
        # Test when the guess is incorrect
        incorrect_guess = [Colour.RED, Colour.RED, Colour.GREEN, Colour.GREEN, Colour.ORANGE]
        result = self.rule_book.check_win(incorrect_guess)
        self.assertFalse(result, "Expected checkWin to return False for an incorrect guess.")

    def test_check_feedback_correct_positions(self):
        # Test correct positions in feedback
        guess = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW, Colour.ORANGE]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_position'], 4, "Expected all positions to be correct.")

    def test_check_feedback_correct_colors(self):
        # Test correct colors in feedback
        guess = [Colour.GREEN, Colour.BLUE, Colour.YELLOW, Colour.RED, Colour.ORANGE]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_color'], 4, "Expected all colors to be correct.")

    def test_check_feedback_mixed_feedback(self):
        # Test a combination of correct positions and colors in feedback
        guess = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.ORANGE, Colour.ORANGE]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_position'], 2, "Expected 2 correct positions.")
        self.assertEqual(feedback['correct_color'], 1, "Expected 1 correct color.")

    # code or guess
    #
    # user entscheidet code länge 4-5
    # user entscheidet menge an farben 2-8
    # user gibt code oder rateversuch anhand der angegebenen codelänge (4-5) und farben anhand der angegeben farbmenge (1-8)
    # user gibt feedback an länge zwischen 0-5 und farben 7-8
    # user gibt game-mode an zwischen 1-2
    #
    def test_check_stone_input_good(self):
        self.assertTrue(check_stone_input(self.good_stone_input_string, 1, self.good_max_code_colours))

    def test_check_stone_input_bad_out_of_bounds(self):
        with self.assertRaises(ValidationError) as exception:
            check_stone_input(self.bad_out_of_bounds_stone_input_string, 1, self.good_max_code_colours)
        exception_message = exception.exception
        print(exception_message)


if __name__ == "__main__":
    unittest.main()
