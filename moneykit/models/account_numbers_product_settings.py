from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountNumbersProductSettings")


@attr.s(auto_attribs=True)
class AccountNumbersProductSettings:
    """
    Attributes:
        required (Union[Unset, bool]): If true, only institutions supporting this product will be available.
        prefetch (Union[Unset, bool]): If true, MoneyKit will begin preparing this data to make it available as soon as
            possible after linking even if `required` is false. If false, MoneyKit will prepare the data after the first
            manual data refresh.
    """

    required: Union[Unset, bool] = False
    prefetch: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        required = self.required
        prefetch = self.prefetch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required is not UNSET:
            field_dict["required"] = required
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        required = d.pop("required", UNSET)

        prefetch = d.pop("prefetch", UNSET)

        account_numbers_product_settings = cls(
            required=required,
            prefetch=prefetch,
        )

        account_numbers_product_settings.additional_properties = d
        return account_numbers_product_settings

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
