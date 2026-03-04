class ValidationError(Exception):
    def __init__(self, message: str):
        self.message = message


class MathError(Exception):
    def __init__(self, message: str):
        self.message = message