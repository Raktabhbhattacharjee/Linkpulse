from app.exceptions.base import AppError


class LinkNotFoundError(AppError):
    status_code = 404

    def __init__(self, short_code: str):
        self.short_code = short_code
        super().__init__(f"Link'{short_code}' was not found")
