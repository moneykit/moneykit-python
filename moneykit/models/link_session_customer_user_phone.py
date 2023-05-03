import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.country import Country
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSessionCustomerUserPhone")


@attr.s(auto_attribs=True)
class LinkSessionCustomerUserPhone:
    """
    Attributes:
        number (str): The user's phone number, preferably in E164 format, including the country code. Example:
            +16175551212.
        country (Union[Unset, None, Country]): An enumeration.
        customer_verified_at (Union[Unset, None, datetime.datetime]): Optional timestamp that marks when you last
            verified this number (such as when the user most
                    recently returned a verification code sent via SMS to this number).
                    Only include this field if you verified the number.  You may supply zeros if the time (but not the date)
                    is unknown. Example: 2023-02-16T00:00:00.
    """

    number: str
    country: Union[Unset, None, Country] = UNSET
    customer_verified_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        country: Union[Unset, None, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value if self.country else None

        customer_verified_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.customer_verified_at, Unset):
            customer_verified_at = self.customer_verified_at.isoformat() if self.customer_verified_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if customer_verified_at is not UNSET:
            field_dict["customer_verified_at"] = customer_verified_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        _country = d.pop("country", UNSET)
        country: Union[Unset, None, Country]
        if _country is None:
            country = None
        elif isinstance(_country, Unset):
            country = UNSET
        else:
            country = Country(_country)

        _customer_verified_at = d.pop("customer_verified_at", UNSET)
        customer_verified_at: Union[Unset, None, datetime.datetime]
        if _customer_verified_at is None:
            customer_verified_at = None
        elif isinstance(_customer_verified_at, Unset):
            customer_verified_at = UNSET
        else:
            customer_verified_at = isoparse(_customer_verified_at)

        link_session_customer_user_phone = cls(
            number=number,
            country=country,
            customer_verified_at=customer_verified_at,
        )

        link_session_customer_user_phone.additional_properties = d
        return link_session_customer_user_phone

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
