from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """
    Attributes:
        city (Union[Unset, None, str]): The city of the address.
        country (Union[Unset, None, str]): The country of the address.
        postal_code (Union[Unset, None, str]): The postal or zip code of the address.
        region (Union[Unset, None, str]): The region or state of the address.
        street (Union[Unset, None, str]): The street of the address.
        primary (Union[Unset, bool]): Indicates if this is the primary address for the account owner.
    """

    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    postal_code: Union[Unset, None, str] = UNSET
    region: Union[Unset, None, str] = UNSET
    street: Union[Unset, None, str] = UNSET
    primary: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        country = self.country
        postal_code = self.postal_code
        region = self.region
        street = self.street
        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if region is not UNSET:
            field_dict["region"] = region
        if street is not UNSET:
            field_dict["street"] = street
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        region = d.pop("region", UNSET)

        street = d.pop("street", UNSET)

        primary = d.pop("primary", UNSET)

        address = cls(
            city=city,
            country=country,
            postal_code=postal_code,
            region=region,
            street=street,
            primary=primary,
        )

        address.additional_properties = d
        return address

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
