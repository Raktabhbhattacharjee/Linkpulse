from app.exceptions.base import AppError


class LinkNotFoundError(AppError):
    def __init__(self, short_code: str):
        self.short_code = short_code

        super().__init__(
            message=f"Link '{short_code}' was not found",
            status_code=404,
            error_code="LINK_NOT_FOUND",
        )
        
        
