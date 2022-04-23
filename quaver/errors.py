class QuaverError(Exception):
    """Base class for exceptions in this module."""
    pass

class APIDown(QuaverError):
    """Exception raised for errors in the API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class InvalidArgumentPassed(QuaverError):
    """Exception raised for errors in the API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message