from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.phone_number_type import PhoneNumberType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumber")


@attr.s(auto_attribs=True)
class PhoneNumber:
    """
    Attributes:
        number (str): A phone number for the account owner. Example: +16175551212.
        type (PhoneNumberType): An enumeration.
        primary (Union[Unset, bool]): Indicates if this is the primary phone number for the account owner.
    """

    number: str
    type: PhoneNumberType
    primary: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        type = self.type.value

        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "type": type,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        type = PhoneNumberType(d.pop("type"))

        primary = d.pop("primary", UNSET)

        phone_number = cls(
            number=number,
            type=type,
            primary=primary,
        )

        phone_number.additional_properties = d
        return phone_number

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
