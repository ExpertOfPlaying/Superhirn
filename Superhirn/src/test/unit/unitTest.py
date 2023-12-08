import unittest

from src.main.python.entities.components.stoneComponent.stone.colourEnum import Colour
from src.main.python.entities.components.userComponent.user.user import User
from src.main.python.entities.components.stoneComponent.stone.stone import Stone
from src.main.python.businesslogic.components.ruleBookComponent.ruleBook.ruleBook import RuleBook


class TestUserRole(unittest.TestCase):
    def test_valid_roles(self):
        # Test, ob die User-Klasse korrekt initialisiert wird, wenn eine gültige Rolle übergeben wird
        user_rater = User("Rater")
        user_coder = User("Coder")

        self.assertEqual(user_rater.role, "Rater")
        self.assertEqual(user_coder.role, "Coder")

    def test_invalid_role(self):
        # Test, ob die User-Klasse ValueError auslöst, wenn eine ungültige Rolle übergeben wird
        with self.assertRaises(ValueError):
            invalid_user = User("InvalidRole")


class TestStoneClass(unittest.TestCase):

    def test_set_get_amount_stones(self):
        stones = Stone(3)
        self.assertEqual(stones.get_amount_colours(), 3)

    def test_set_get_amount_stones_exception_over(self):
        with self.assertRaises(ValueError):
            stones = Stone(9)

    def test_set_get_amount_stones_exception_under(self):
        with self.assertRaises(ValueError):
            stones = Stone(1)

    def test_get_colour(self):
        stones = Stone(3)
        self.assertEqual(stones.get_colour(0), Colour.RED)


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
