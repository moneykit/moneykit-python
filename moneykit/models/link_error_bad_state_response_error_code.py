from enum import Enum


class LinkErrorBadStateResponseErrorCode(str, Enum):
    LINK_ERROR_BAD_STATE = "link_error.bad_state"

    def __str__(self) -> str:
        return str(self.value)
