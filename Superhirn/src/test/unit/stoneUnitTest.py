import unittest
from src.python.entities.stoneComponent.stone import Stone
from src.python.entities.stoneComponent.colourEnum import Colour


class TestStoneClass(unittest.TestCase):

    def setUp(self):
        self.stone = Stone(1)

    # # ---------------------------------------------------get_colour---------------------------------------

    def test_get_correct_colour(self):
        self.assertEqual(self.stone.colour, Colour.RED)

    def test_get_correct_value(self):
        self.assertEqual(self.stone.colour.value, Colour.RED.value)


if __name__ == '__main__':
    unittest.main()
