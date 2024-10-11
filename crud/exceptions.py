import http
from typing import Dict
from fastapi import HTTPException

class BaseHTTPException(HTTPException):
    status_code: int
    message: str
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(self.status_code, self.message, headers)

class ObjectDoesNotExistsException(BaseHTTPException):
    status_code = http.HTTPStatus.NOT_FOUND
    message = "Invalid ID"
