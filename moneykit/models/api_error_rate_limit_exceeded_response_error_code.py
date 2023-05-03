from enum import Enum


class APIErrorRateLimitExceededResponseErrorCode(str, Enum):
    API_ERROR_RATE_LIMIT_EXCEEDED = "api_error.rate_limit_exceeded"

    def __str__(self) -> str:
        return str(self.value)
