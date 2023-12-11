import unittest
from src.main.python.entities.stoneComponent.stone import Stone
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestStoneClass(unittest.TestCase):

    def setUp(self):
        self.stones = Stone(7)

    # ---------------------------------------------------set_colour---------------------------------------

    def test_set_stones(self):
        self.assertEqual(7, len(self.stones.stones))

    def test_set_stones_exception_none(self):
        with self.assertRaises(TypeError) as exception:
            self.stones.stones = None
        exception_message = exception.exception
        print(exception_message)

    def test_set_stones_exception_empty(self):
        with self.assertRaises(TypeError) as exception:
            stones = Stone()
        exception_message = exception.exception
        print(exception_message)

    def test_set_colours_exception_over(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.stones = 9
        exception_message = exception.exception
        print(exception_message)

    def test_set_colours_exception_under(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.stones = 1
        exception_message = exception.exception
        print(exception_message)

    def test_set_colours_exception_not_int(self):
        with self.assertRaises(TypeError) as exception:
            self.stones.stones = "b"
        exception_message = exception.exception
        print(exception_message)

    # ---------------------------------------------------get_colour---------------------------------------

    def test_get_colour(self):
        self.assertEqual(self.stones.get_colour(1), Colour.RED)

    def test_get_colour_exception_over(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.get_colour(8)
        exception_message = exception.exception
        print(exception_message)

    def test_get_colour_exception_under(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.get_colour(0)
        exception_message = exception.exception
        print(exception_message)

    def test_get_colour_exception_not_int(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.get_colour("b")
        exception_message = exception.exception
        print(exception_message)

    def test_get_colour_exception_empty(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.get_colour()
        exception_message = exception.exception
        print(exception_message)

    def test_get_colour_exception_none(self):
        with self.assertRaises(ValueError) as exception:
            self.stones.get_colour(None)
        exception_message = exception.exception
        print(exception_message)


if __name__ == '__main__':
    unittest.main()
