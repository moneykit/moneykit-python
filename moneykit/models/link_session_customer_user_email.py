import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSessionCustomerUserEmail")


@attr.s(auto_attribs=True)
class LinkSessionCustomerUserEmail:
    """
    Attributes:
        address (str): The user's email address.
        customer_verified_at (Union[Unset, None, datetime.datetime]): Optional timestamp that marks when you last
            verified this email (such as when the user most
                    recently clicked a verification url sent to this address).
                    Only include this field if you verified the address.  You may supply zeros if the time (but not the
            date)
                    is unknown. Example: 2023-02-16T00:00:00.
    """

    address: str
    customer_verified_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        customer_verified_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.customer_verified_at, Unset):
            customer_verified_at = self.customer_verified_at.isoformat() if self.customer_verified_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )
        if customer_verified_at is not UNSET:
            field_dict["customer_verified_at"] = customer_verified_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        _customer_verified_at = d.pop("customer_verified_at", UNSET)
        customer_verified_at: Union[Unset, None, datetime.datetime]
        if _customer_verified_at is None:
            customer_verified_at = None
        elif isinstance(_customer_verified_at, Unset):
            customer_verified_at = UNSET
        else:
            customer_verified_at = isoparse(_customer_verified_at)

        link_session_customer_user_email = cls(
            address=address,
            customer_verified_at=customer_verified_at,
        )

        link_session_customer_user_email.additional_properties = d
        return link_session_customer_user_email

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
