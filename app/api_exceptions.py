from fastapi import HTTPException
from typing import Optional

class BaseAPIException(HTTPException):
    def __init__(self,
        status_code: int,
        detail: str,
        error_code: Optional[str] = None,
        extra: Optional[dict] = None
    ):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.extra = extra or {}


class NotFoundException(BaseAPIException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(404, detail, error_code="not_found")


class ValidationException(BaseAPIException):
    def __init__(self, detail: str, errors: Optional[list] = None):
        super().__init__(422, detail, error_code="validation_error")
        self.extra["fields"] = errors or []


class BusinessLogicException(BaseAPIException):
    def __init__(self, detail: str):
        super().__init__(409, detail, error_code="business_error")
