from .colourEnum import Colour


class Stone:
    def __init__(self, colour):
        self._colour = colour

    @property
    def colour(self):
        return Colour(self._colour)

    @colour.setter
    def colour(self, value):
        self._colour = Colour(value)
