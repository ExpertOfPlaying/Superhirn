from src.main.python.entities.stoneComponent.colourEnum import Colour


class Stone:
    def __init__(self, colour):
        self.colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if not value:
            raise ValueError("Empty colour")
        value = Colour(value)
        if not isinstance(value, Colour):
            raise StoneError("Ungültige Farbe")
        self._colour = value