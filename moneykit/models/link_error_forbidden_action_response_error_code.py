from enum import Enum


class LinkErrorForbiddenActionResponseErrorCode(str, Enum):
    LINK_ERROR_FORBIDDEN_ACTION = "link_error.forbidden_action"

    def __str__(self) -> str:
        return str(self.value)
