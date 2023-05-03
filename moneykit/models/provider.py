from enum import Enum


class Provider(str, Enum):
    FINICITY = "finicity"
    MONEYKIT = "moneykit"
    MX = "mx"
    PLAID = "plaid"
    YODLEE = "yodlee"

    def __str__(self) -> str:
        return str(self.value)
