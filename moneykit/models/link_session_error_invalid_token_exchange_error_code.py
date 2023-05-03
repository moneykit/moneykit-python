from enum import Enum


class LinkSessionErrorInvalidTokenExchangeErrorCode(str, Enum):
    LINK_SESSION_ERROR_INVALID_TOKEN_EXCHANGE = "link_session_error.invalid_token_exchange"

    def __str__(self) -> str:
        return str(self.value)
