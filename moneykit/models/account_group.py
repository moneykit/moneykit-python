import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="AccountGroup")


@attr.s(auto_attribs=True)
class AccountGroup:
    """
    Attributes:
        accounts (List['Account']):
        last_synced_at (Union[Unset, None, datetime.datetime]): An ISO-8601 timestamp indicating the last time that the
            account was updated. Example: 2023-02-16T09:14:11.
    """

    accounts: List["Account"]
    last_synced_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()

            accounts.append(accounts_item)

        last_synced_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat() if self.last_synced_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
            }
        )
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: Union[Unset, None, datetime.datetime]
        if _last_synced_at is None:
            last_synced_at = None
        elif isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = isoparse(_last_synced_at)

        account_group = cls(
            accounts=accounts,
            last_synced_at=last_synced_at,
        )

        account_group.additional_properties = d
        return account_group

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
