import unittest

from src.main.python.entities.userComponent.user import User


class TestUserRole(unittest.TestCase):

    def setUp(self):
        self.user = User("Rater", "Player_one")

    def test_get_role(self):
        self.assertEqual(self.user.role, "Rater")

    def test_set_roles(self):
        self.user.role = "Coder"
        self.assertEqual(self.user.role, "Coder")

    def test_get_name(self):
        self.assertEqual(self.user.name, "Player_one")

    def test_set_name(self):
        self.user.name = "Player_two"
        self.assertEqual(self.user.name, "Player_two")


if __name__ == '__main__':
    unittest.main()
