class AppError(Exception):
    """
    Base class for all business/application exceptions.
    """

    status_code = 500

    def __init__(self, message: str, status_code: int, error_code: str):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(message)
