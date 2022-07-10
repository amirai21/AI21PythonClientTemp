class AI21HttpException(Exception):
    def __init__(self, status_code: int, details: str):
        super().__init__(details)
        self.details = details
        self.status_code = status_code

    def __str__(self) -> str:
        return f'{type(self).__name__} Got http status code: {self.status_code}. details: {self.details}'


class BadRequest(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(400, details)


class Unauthorized(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(401, details)


class UnprocessableEntity(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(422, details)


class TooManyRequests(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(429, details)


class ServerError(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(500, details)


class ServiceUnavailable(AI21HttpException):
    def __init__(self, details: str):
        super().__init__(500, details)


class InputValidationException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.message = message
        self.errors = errors

    def __str__(self) -> str:
        return f'{type(self).__name__} message: {self.message} errors: {self.errors}'
