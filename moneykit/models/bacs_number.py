from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BacsNumber")


@attr.s(auto_attribs=True)
class BacsNumber:
    """
    Attributes:
        account_number (str): The account number.
        sort_code (str): The sort code.
    """

    account_number: str
    sort_code: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number = self.account_number
        sort_code = self.sort_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_number": account_number,
                "sort_code": sort_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("account_number")

        sort_code = d.pop("sort_code")

        bacs_number = cls(
            account_number=account_number,
            sort_code=sort_code,
        )

        bacs_number.additional_properties = d
        return bacs_number

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
