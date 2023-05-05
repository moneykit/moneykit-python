import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_numbers_product_settings import AccountNumbersProductSettings


T = TypeVar("T", bound="AccountNumbersLinkProduct")


@attr.s(auto_attribs=True)
class AccountNumbersLinkProduct:
    """
    Attributes:
        settings (AccountNumbersProductSettings):
        refreshed_at (Union[Unset, None, datetime.datetime]): An ISO-8601 timestamp indicating the last time that the
            product was updated. Example: 2023-02-16T09:14:11.
        last_attempted_at (Union[Unset, None, datetime.datetime]): An ISO-8601 timestamp indicating the last time that
            the product was attempted. Example: 2023-02-16T09:14:11.
    """

    settings: "AccountNumbersProductSettings"
    refreshed_at: Union[Unset, None, datetime.datetime] = UNSET
    last_attempted_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings = self.settings.to_dict()

        refreshed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.refreshed_at, Unset):
            refreshed_at = self.refreshed_at.isoformat() if self.refreshed_at else None

        last_attempted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_attempted_at, Unset):
            last_attempted_at = self.last_attempted_at.isoformat() if self.last_attempted_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )
        if refreshed_at is not UNSET:
            field_dict["refreshed_at"] = refreshed_at
        if last_attempted_at is not UNSET:
            field_dict["last_attempted_at"] = last_attempted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_numbers_product_settings import AccountNumbersProductSettings

        d = src_dict.copy()
        settings = AccountNumbersProductSettings.from_dict(d.pop("settings"))

        _refreshed_at = d.pop("refreshed_at", UNSET)
        refreshed_at: Union[Unset, None, datetime.datetime]
        if _refreshed_at is None:
            refreshed_at = None
        elif isinstance(_refreshed_at, Unset):
            refreshed_at = UNSET
        else:
            refreshed_at = isoparse(_refreshed_at)

        _last_attempted_at = d.pop("last_attempted_at", UNSET)
        last_attempted_at: Union[Unset, None, datetime.datetime]
        if _last_attempted_at is None:
            last_attempted_at = None
        elif isinstance(_last_attempted_at, Unset):
            last_attempted_at = UNSET
        else:
            last_attempted_at = isoparse(_last_attempted_at)

        account_numbers_link_product = cls(
            settings=settings,
            refreshed_at=refreshed_at,
            last_attempted_at=last_attempted_at,
        )

        account_numbers_link_product.additional_properties = d
        return account_numbers_link_product

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
