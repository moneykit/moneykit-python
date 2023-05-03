from enum import Enum


class InstitutionErrorNotFoundResponseErrorCode(str, Enum):
    INSTITUTION_ERROR_NOT_FOUND = "institution_error.not_found"

    def __str__(self) -> str:
        return str(self.value)
