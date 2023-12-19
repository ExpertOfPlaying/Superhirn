from src.main.python.entities.stoneComponent.colourEnum import Colour


class Stone:
    def __init__(self, colour):
        self.colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        value = Colour(value)
        self._colour = value
