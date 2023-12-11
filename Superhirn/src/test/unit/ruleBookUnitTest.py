import unittest

from src.main.python.businesslogic.ruleBookComponent.ruleBook import RuleBook
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestRuleBook(unittest.TestCase):
    def setUp(self):
        # Set up a RuleBook instance with a secret code
        self.secret_code = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW]
        self.rule_book = RuleBook(self.secret_code)

    def test_check_win_correct_guess(self):
        # Test when the guess is correct
        correct_guess = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW]
        result = self.rule_book.check_win(correct_guess)
        self.assertTrue(result, "Expected checkWin to return True for a correct guess.")

    def test_check_win_incorrect_guess(self):
        # Test when the guess is incorrect
        incorrect_guess = [Colour.RED, Colour.RED, Colour.GREEN, Colour.GREEN]
        result = self.rule_book.check_win(incorrect_guess)
        self.assertFalse(result, "Expected checkWin to return False for an incorrect guess.")

    def test_check_feedback_correct_positions(self):
        # Test correct positions in feedback
        guess = [Colour.RED, Colour.GREEN, Colour.BLUE, Colour.YELLOW]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_position'], 4, "Expected all positions to be correct.")

    def test_check_feedback_correct_colors(self):
        # Test correct colors in feedback
        guess = [Colour.GREEN, Colour.BLUE, Colour.YELLOW, Colour.RED]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_color'], 4, "Expected all colors to be correct.")

    def test_check_feedback_mixed_feedback(self):
        # Test a combination of correct positions and colors in feedback
        guess = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.ORANGE]
        feedback = self.rule_book.check_feedback(guess)
        self.assertEqual(feedback['correct_position'], 2, "Expected 2 correct positions.")
        self.assertEqual(feedback['correct_color'], 1, "Expected 1 correct color.")


if __name__ == "main":
    unittest.main()
