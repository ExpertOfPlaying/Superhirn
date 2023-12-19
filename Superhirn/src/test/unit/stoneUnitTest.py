import unittest
from src.main.python.entities.stoneComponent.stone import Stone
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestStoneClass(unittest.TestCase):

    # # ---------------------------------------------------get_colour---------------------------------------

    def test_get_correct_colour(self):
        stone = Stone(1)
        self.assertEqual(stone.colour, Colour.RED)

    def test_get_correct_value(self):
        stone = Stone(1)
        self.assertEqual(stone.colour.value, Colour.RED.value)


if __name__ == '__main__':
    unittest.main()
