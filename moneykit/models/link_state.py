from enum import Enum


class LinkState(str, Enum):
    AWAITING_TOKEN_EXCHANGE = "awaiting_token_exchange"
    CONNECTED = "connected"
    CONNECTING = "connecting"
    DELETED = "deleted"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
