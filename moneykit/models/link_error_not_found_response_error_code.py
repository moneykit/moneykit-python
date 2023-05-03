from enum import Enum


class LinkErrorNotFoundResponseErrorCode(str, Enum):
    LINK_ERROR_NOT_FOUND = "link_error.not_found"

    def __str__(self) -> str:
        return str(self.value)
