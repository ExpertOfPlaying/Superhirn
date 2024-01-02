import unittest

from src.python.entities.userComponent.user import User
from src.python.entities.userComponent.roleEnum import Role


class TestUserRole(unittest.TestCase):

    def setUp(self):
        self.coder = 1
        self.guesser = 2
        self.userGuesser = User(self.guesser, "Player_two")
        self.userCoder = User(self.coder, "Player_one")

    def test_get_role(self):
        self.assertEqual(self.userGuesser.role, Role.Rater)

    def test_set_roles(self):
        self.userGuesser.role = 1
        self.assertEqual(self.userGuesser.role, Role.Coder)

    def test_get_name(self):
        self.assertEqual(self.userCoder.name, "Player_one")

    def test_set_name(self):
        self.userCoder.name = "Player_two"
        self.assertEqual(self.userCoder.name, "Player_two")


if __name__ == '__main__':
    unittest.main()
