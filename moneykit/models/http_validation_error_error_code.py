from enum import Enum


class HTTPValidationErrorErrorCode(str, Enum):
    API_ERROR_REQUEST_VALIDATION_FAILED = "api_error.request.validation_failed"

    def __str__(self) -> str:
        return str(self.value)
