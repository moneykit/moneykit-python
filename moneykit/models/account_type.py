from enum import Enum


class AccountType(str, Enum):
    CREDIT_CARD = "credit_card"
    DEPOSITORY_CASH = "depository.cash"
    DEPOSITORY_CHECKING = "depository.checking"
    DEPOSITORY_OTHER = "depository.other"
    DEPOSITORY_PREPAID = "depository.prepaid"
    DEPOSITORY_SAVINGS = "depository.savings"
    INVESTMENT = "investment"
    LOAN_GENERAL = "loan.general"
    LOAN_MORTGAGE = "loan.mortgage"
    LOAN_OTHER = "loan.other"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
