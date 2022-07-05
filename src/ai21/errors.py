class AI21Exception(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class InputValidationException(AI21Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
