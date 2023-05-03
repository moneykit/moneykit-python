from enum import Enum


class LinkSessionErrorForbiddenConfigResponseErrorCode(str, Enum):
    LINK_SESSION_ERROR_FORBIDDEN_CONFIG = "link_session_error.forbidden_config"

    def __str__(self) -> str:
        return str(self.value)
