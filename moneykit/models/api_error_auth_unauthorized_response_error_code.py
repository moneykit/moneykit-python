from enum import Enum


class APIErrorAuthUnauthorizedResponseErrorCode(str, Enum):
    API_ERROR_AUTH_UNAUTHORIZED = "api_error.auth.unauthorized"

    def __str__(self) -> str:
        return str(self.value)
