from src.main.python.entities.stoneComponent.stone import Stone


class Board:
    def __init__(self, code_max_length, max_attempts, attempts=0, guessed_code=0, answer_code=0, feedback=0):
        self.code_max_length = code_max_length
        self.max_attempts = max_attempts
        self.attempts = attempts
        self.guessed_code = guessed_code
        self.answer_code = answer_code
        self.feedback = feedback


    @property
    def guessed_code(self):
        return self._guessed_code

    @guessed_code.setter
    def guessed_code(self, values):
        if len(values) > self.code_max_length < len(values):
            raise ValueError("Code nicht in den richtigen Länge")
        stones = []
        for value in values:
            try:
                stones.append(self.create_stone(value))
            except ValueError:
                raise ValueError("Code enthält ungültige Farben")
        self._guessed_code = stones

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        self._attempts = attempts

    def create_stone(self, value):
        if not isinstance(value, Stone):
            return Stone(value)
        else:
            return value