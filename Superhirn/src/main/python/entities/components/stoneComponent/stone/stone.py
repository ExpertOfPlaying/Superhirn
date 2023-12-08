from src.main.python.entities.components.stoneComponent.stone.colourEnum import Colour


class Stone(object):
    def __init__(self, amount_stones):
        self._amount_stones = 0
        self._stones = []
        self.set_amount_stones(amount_stones)

    def set_amount_stones(self, amount_stones):
        if amount_stones > len(Colour):
            raise ValueError("Number of stones cannot exceed the number of colors in the enum.")

        self._amount_stones = amount_stones
        self._stones = [colour for colour in Colour][:amount_stones]

    def get_amount_stones(self):
        return self._amount_stones
