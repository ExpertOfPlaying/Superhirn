import unittest
from src.main.python.entities.stoneComponent.stone import Stone
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestStoneClass(unittest.TestCase):


    # ---------------------------------------------------set_colour---------------------------------------

    def test_create_stone_with_color_enum(self):
        stone = Stone(Colour.RED)
        self.assertTrue(stone)

    def test_create_stone_with_correct_int_value(self):
        stone = Stone(5)
        self.assertTrue(stone)

    def test_create_stone_with_invalid_int_value(self):
        with self.assertRaises(ValueError) as exception:
            stone = Stone(10)
        with self.assertRaises(ValueError) as exception:
            stone = Stone(-1)

    # # ---------------------------------------------------get_colour---------------------------------------

    def test_get_correct_colour(self):
        stone = Stone(Colour.RED)
        self.assertEqual(stone.colour, Colour.RED)
        self.assertEqual(stone.colour.value, Colour.RED.value)
        self.assertNotEquals(stone.colour, Colour.GREEN)


if __name__ == '__main__':
    unittest.main()
