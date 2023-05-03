from enum import Enum


class LinkError(str, Enum):
    AUTH_EXPIRED = "auth_expired"
    INCOMPLETE = "incomplete"
    INSTITUTION_ERROR = "institution_error"
    PAYMENT_ERROR = "payment_error"
    PROVIDER_ERROR = "provider_error"
    SYSTEM_ERROR = "system_error"
    USER_ERROR = "user_error"

    def __str__(self) -> str:
        return str(self.value)
