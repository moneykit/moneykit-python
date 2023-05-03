from enum import Enum


class PhoneNumberType(str, Enum):
    HOME = "home"
    MOBILE = "mobile"
    OTHER = "other"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
