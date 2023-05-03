from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoneyLinkFeatures")


@attr.s(auto_attribs=True)
class MoneyLinkFeatures:
    """
    Attributes:
        bug_reporter (Union[Unset, bool]): If enabled, the user can perform a gesture that displays a bug reporter
            directly in the SDK's UI.
        enable_money_id (Union[Unset, bool]): If enabled, the user can register for, or login into, Money ID.
    """

    bug_reporter: Union[Unset, bool] = False
    enable_money_id: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bug_reporter = self.bug_reporter
        enable_money_id = self.enable_money_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bug_reporter is not UNSET:
            field_dict["bug_reporter"] = bug_reporter
        if enable_money_id is not UNSET:
            field_dict["enable_money_id"] = enable_money_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bug_reporter = d.pop("bug_reporter", UNSET)

        enable_money_id = d.pop("enable_money_id", UNSET)

        money_link_features = cls(
            bug_reporter=bug_reporter,
            enable_money_id=enable_money_id,
        )

        money_link_features.additional_properties = d
        return money_link_features

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
