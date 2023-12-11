from src.main.python.entities.stoneComponent.colourEnum import Colour


def exception_handler_amount_colours(amount_colours):
    if not isinstance(amount_colours, int):
        raise TypeError("The amount of colours must be an integer.")
    if amount_colours < 2:
        raise ValueError("The number of colours cannot be less than the minimum number of colors (2).")
    if amount_colours > len(Colour):
        raise ValueError("The number of colours cannot exceed the maximum amount of colours (8).")


class Stone(object):
    def __init__(self, amount_colours=None):
        exception_handler_amount_colours(amount_colours)
        self.stones = amount_colours

    @property
    # Debugging method
    def stones(self):
        return self._stones

    @stones.setter
    def stones(self, amount_colours):
        exception_handler_amount_colours(amount_colours)
        self._stones = [colour for colour in Colour][:amount_colours]

    # Get the colour of a postion
    def get_colour(self, position=None):
        if isinstance(position, int) and 1 <= position <= len(self.stones):
            position = position - 1
            return self._stones[position]
        else:
            raise ValueError("No such colour.")
