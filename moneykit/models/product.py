from enum import Enum


class Product(str, Enum):
    ACCOUNTS = "accounts"
    ACCOUNT_NUMBERS = "account_numbers"
    IDENTITY = "identity"
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
