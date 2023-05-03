from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.country import Country
from ..types import UNSET, Unset

T = TypeVar("T", bound="Institution")


@attr.s(auto_attribs=True)
class Institution:
    """
    Attributes:
        institution_id (str): MoneyKit's unique ID for this institution. Example: chase.
        name (str): The name of the institution. Example: Chase.
        country (Country): An enumeration.
        color (str): The primary color of this institution, represented as hexcode. Example: #0A89FF.
        is_featured (bool): True for institutions that should be visually promoted to the end-user.
        domain (Union[Unset, None, str]): The domain of the institution's customer-facing website. Example: chase.com.
        color_dark (Union[Unset, None, str]): The dark-mode primary color of this institution, represented as hexcode.
            Example: #0A89FF.
    """

    institution_id: str
    name: str
    country: Country
    color: str
    is_featured: bool
    domain: Union[Unset, None, str] = UNSET
    color_dark: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        institution_id = self.institution_id
        name = self.name
        country = self.country.value

        color = self.color
        is_featured = self.is_featured
        domain = self.domain
        color_dark = self.color_dark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institution_id": institution_id,
                "name": name,
                "country": country,
                "color": color,
                "is_featured": is_featured,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if color_dark is not UNSET:
            field_dict["color_dark"] = color_dark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        institution_id = d.pop("institution_id")

        name = d.pop("name")

        country = Country(d.pop("country"))

        color = d.pop("color")

        is_featured = d.pop("is_featured")

        domain = d.pop("domain", UNSET)

        color_dark = d.pop("color_dark", UNSET)

        institution = cls(
            institution_id=institution_id,
            name=name,
            country=country,
            color=color,
            is_featured=is_featured,
            domain=domain,
            color_dark=color_dark,
        )

        institution.additional_properties = d
        return institution

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
