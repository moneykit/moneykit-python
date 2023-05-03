import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicAccountDetails")


@attr.s(auto_attribs=True)
class BasicAccountDetails:
    """
    Attributes:
        name (str): The account name, according to the institution.  Note that some institutions allow
                    the end user to nickname the account; in such cases this field may be the name assigned by the user
            Example: Premier Checking.
        institution_id (str):
        link_id (str): The unique ID of the link this account belongs to.
        last_synced_at (Union[Unset, None, datetime.datetime]): An ISO-8601 timestamp indicating the last time that the
            account was updated. Example: 2023-02-16T09:14:11.
    """

    name: str
    institution_id: str
    link_id: str
    last_synced_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        institution_id = self.institution_id
        link_id = self.link_id
        last_synced_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat() if self.last_synced_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "institution_id": institution_id,
                "link_id": link_id,
            }
        )
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        institution_id = d.pop("institution_id")

        link_id = d.pop("link_id")

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: Union[Unset, None, datetime.datetime]
        if _last_synced_at is None:
            last_synced_at = None
        elif isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = isoparse(_last_synced_at)

        basic_account_details = cls(
            name=name,
            institution_id=institution_id,
            link_id=link_id,
            last_synced_at=last_synced_at,
        )

        basic_account_details.additional_properties = d
        return basic_account_details

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
