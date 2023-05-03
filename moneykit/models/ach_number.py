from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AchNumber")


@attr.s(auto_attribs=True)
class AchNumber:
    """
    Attributes:
        account_number (str): The account number.
        routing_number (str): The routing number.
        wire_routing_number (Union[Unset, None, str]): The wire routing number.
    """

    account_number: str
    routing_number: str
    wire_routing_number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number = self.account_number
        routing_number = self.routing_number
        wire_routing_number = self.wire_routing_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_number": account_number,
                "routing_number": routing_number,
            }
        )
        if wire_routing_number is not UNSET:
            field_dict["wire_routing_number"] = wire_routing_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("account_number")

        routing_number = d.pop("routing_number")

        wire_routing_number = d.pop("wire_routing_number", UNSET)

        ach_number = cls(
            account_number=account_number,
            routing_number=routing_number,
            wire_routing_number=wire_routing_number,
        )

        ach_number.additional_properties = d
        return ach_number

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
