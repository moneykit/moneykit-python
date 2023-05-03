from enum import Enum


class Country(str, Enum):
    CA = "CA"
    GB = "GB"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
