from enum import Enum


class SupportedVersion(str, Enum):
    VALUE_0 = "2023-02-18"

    def __str__(self) -> str:
        return str(self.value)
