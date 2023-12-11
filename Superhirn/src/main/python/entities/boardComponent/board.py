def exception_handler_code_length(code_length):
    if not isinstance(code_length, int):
        raise TypeError("The length of the code must be an integer.")
    if code_length < 4:
        raise ValueError("The length of the code cannot be less than the minimum length (4).")
    if code_length > 5:
        raise ValueError("The length of the code cannot exceed the the maximum length (5).")


def exception_handler_attempts(attempts):
    if not isinstance(attempts, int):
        raise TypeError("The number of attempts must be an integer.")
    if attempts < 1:
        raise ValueError("The number of attempts cannot be less than the minimum length (1).")
    if attempts > 10:
        raise ValueError("The number of attempts cannot exceed the maximum amount attempts (10).")


class Board(object):
    def __init__(self, code_length=None, attempts=None):
        exception_handler_code_length(code_length)
        exception_handler_attempts(attempts)
        self.code_length = code_length
        self.attempts = attempts

    @property
    def code_length(self):
        return self._code_length

    @code_length.setter
    def code_length(self, code_length):
        exception_handler_code_length(code_length)
        self._code_length = code_length

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        exception_handler_attempts(attempts)
        self._attempts = attempts
