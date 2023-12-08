from src.main.python.entities.components.stoneComponent.stone.colourEnum import Colour


class Stone(object):
    def __init__(self, amount_colours):
        self._amount_colours = 0
        self._stones = []
        self.set_amount_colours(amount_colours)

    def set_amount_colours(self, amount_colours):
        if amount_colours > len(Colour):
            raise ValueError("Number of colours cannot exceed the maximum amount of colours (8).")
        if amount_colours < 2:
            raise ValueError("Number of colours cannot be less than the minimum number of colors (2).")

        self._amount_colours = amount_colours
        self._stones = [colour for colour in Colour][:amount_colours]

    def get_amount_colours(self):
        return self._amount_colours

    def get_colour(self, position):
        return self._stones[position]
