from enum import Enum


class LinkErrorDeletedResponseErrorCode(str, Enum):
    LINK_ERROR_DELETED = "link_error.deleted"

    def __str__(self) -> str:
        return str(self.value)
