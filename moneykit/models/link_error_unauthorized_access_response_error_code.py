from enum import Enum


class LinkErrorUnauthorizedAccessResponseErrorCode(str, Enum):
    LINK_ERROR_UNAUTHORIZED_ACCESS = "link_error.unauthorized_access"

    def __str__(self) -> str:
        return str(self.value)
