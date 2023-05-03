from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.email import Email
    from ..models.phone_number import PhoneNumber


T = TypeVar("T", bound="Owner")


@attr.s(auto_attribs=True)
class Owner:
    """
    Attributes:
        names (List[str]): A list of names for the account owner.
        addresses (List['Address']): A list of addresses for the account owner. Some addresses can appear as incomplete.
        phone_numbers (List['PhoneNumber']): A list of phone numbers for the account owner.
        emails (List['Email']): A list of email addresses for the account owner.
    """

    names: List[str]
    addresses: List["Address"]
    phone_numbers: List["PhoneNumber"]
    emails: List["Email"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        names = self.names

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item = addresses_item_data.to_dict()

            addresses.append(addresses_item)

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()

            phone_numbers.append(phone_numbers_item)

        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()

            emails.append(emails_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "names": names,
                "addresses": addresses,
                "phone_numbers": phone_numbers,
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.email import Email
        from ..models.phone_number import PhoneNumber

        d = src_dict.copy()
        names = cast(List[str], d.pop("names"))

        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:
            addresses_item = Address.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = PhoneNumber.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = Email.from_dict(emails_item_data)

            emails.append(emails_item)

        owner = cls(
            names=names,
            addresses=addresses,
            phone_numbers=phone_numbers,
            emails=emails,
        )

        owner.additional_properties = d
        return owner

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
