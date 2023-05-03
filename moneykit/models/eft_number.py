from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EftNumber")


@attr.s(auto_attribs=True)
class EftNumber:
    """
    Attributes:
        account_number (str): The account number.
        institution_number (str): The institution number.
        branch_number (str): The branch number.
    """

    account_number: str
    institution_number: str
    branch_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number = self.account_number
        institution_number = self.institution_number
        branch_number = self.branch_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_number": account_number,
                "institution_number": institution_number,
                "branch_number": branch_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("account_number")

        institution_number = d.pop("institution_number")

        branch_number = d.pop("branch_number")

        eft_number = cls(
            account_number=account_number,
            institution_number=institution_number,
            branch_number=branch_number,
        )

        eft_number.additional_properties = d
        return eft_number

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
