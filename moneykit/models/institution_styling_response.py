from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstitutionStylingResponse")


@attr.s(auto_attribs=True)
class InstitutionStylingResponse:
    """
    Attributes:
        name (str): The name of the institution. Example: Chase.
        color (str): The primary color of this institution, represented as hexcode. Example: #0A89FF.
        avatar (str): URL to the avatar image for this institution Example: https://cdn.cloudfront.net/avatar.png.
        domain (Union[Unset, None, str]): The domain of the institution's customer-facing website. Example: chase.com.
        color_dark (Union[Unset, None, str]): The dark-mode primary color of this institution, represented as hexcode.
            Example: #0A89FF.
        avatar_dark (Union[Unset, None, str]): URL to the dark-mode avatar image for this institution Example:
            https://cdn.cloudfront.net/avatar-dark.png.
        logo (Union[Unset, None, str]): URL to the logo image for this institution Example:
            https://cdn.cloudfront.net/logo.png.
        logo_dark (Union[Unset, None, str]): URL to the dark-mode logo image for this institution Example:
            https://cdn.cloudfront.net/logo-dark.png.
    """

    name: str
    color: str
    avatar: str
    domain: Union[Unset, None, str] = UNSET
    color_dark: Union[Unset, None, str] = UNSET
    avatar_dark: Union[Unset, None, str] = UNSET
    logo: Union[Unset, None, str] = UNSET
    logo_dark: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color
        avatar = self.avatar
        domain = self.domain
        color_dark = self.color_dark
        avatar_dark = self.avatar_dark
        logo = self.logo
        logo_dark = self.logo_dark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "color": color,
                "avatar": avatar,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if color_dark is not UNSET:
            field_dict["color_dark"] = color_dark
        if avatar_dark is not UNSET:
            field_dict["avatar_dark"] = avatar_dark
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logo_dark is not UNSET:
            field_dict["logo_dark"] = logo_dark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = d.pop("color")

        avatar = d.pop("avatar")

        domain = d.pop("domain", UNSET)

        color_dark = d.pop("color_dark", UNSET)

        avatar_dark = d.pop("avatar_dark", UNSET)

        logo = d.pop("logo", UNSET)

        logo_dark = d.pop("logo_dark", UNSET)

        institution_styling_response = cls(
            name=name,
            color=color,
            avatar=avatar,
            domain=domain,
            color_dark=color_dark,
            avatar_dark=avatar_dark,
            logo=logo,
            logo_dark=logo_dark,
        )

        institution_styling_response.additional_properties = d
        return institution_styling_response

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
