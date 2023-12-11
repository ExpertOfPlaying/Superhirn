import unittest

from src.main.python.entities.userComponent.user import User


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


if __name__ == '__main__':
    unittest.main()
