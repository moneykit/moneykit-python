from enum import Enum


class APIErrorAuthExpiredAccessTokenResponseErrorCode(str, Enum):
    API_ERROR_AUTH_EXPIRED_ACCESS_TOKEN = "api_error.auth.expired_access_token"

    def __str__(self) -> str:
        return str(self.value)
