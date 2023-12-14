from src.main.python.entities.stoneComponent.stone import Stone


# static methods
def create_stone(value):
    if not isinstance(value, Stone):
        return Stone(value)
    else:
        return value

def create_feedback(value):
    if not isinstance(value, Stone):
        return Stone(value)
    else:
        return value


class Board:
    def __init__(self, code_max_length, max_attempts, attempts=0, guessed_code=0, answer_code=0, feedback=0):
        self.code_max_length = code_max_length
        self.max_attempts = max_attempts
        self.attempts = attempts
        self.guessed_code = guessed_code
        self.answer_code = answer_code
        self.feedback = feedback


    @property
    def code_max_length(self):
        return self._code_max_length

    @code_max_length.setter
    def code_max_length(self, value):
        self._code_max_length = value

    @property
    def max_attempts(self):
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, value):
        self._max_attempts = value

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, value):
        if value > self.max_attempts:
            raise ValueError("Maximale Anzahl an Versuchen erreicht")
        self._attempts = value

    @property
    def guessed_code(self):
        return self._guessed_code

    @guessed_code.setter
    def guessed_code(self, values):
        self.check_code_length(values)
        stones = []
        for value in values:
            try:
                stones.append(create_stone(value))
            except ValueError:
                raise ValueError("Code enthält ungültige Farben")
        self._guessed_code = stones

    @property
    def answer_code(self):
        return self._answer_code

    @answer_code.setter
    def answer_code(self, values):
        self.check_code_length(values)
        stones = []
        for value in values:
            try:
                stones.append(create_stone(value))
            except ValueError:
                raise ValueError("Code enthält ungültige Farben")
        self._guessed_code = stones

    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, values):
        self.check_code_length(values)
        self._feedback =

    def check_code_length(self, code):
        if len(code) > self.code_max_length < len(code):
            raise ValueError("Code nicht in den richtigen Länge")