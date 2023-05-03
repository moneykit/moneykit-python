from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionsProductSettings")


@attr.s(auto_attribs=True)
class TransactionsProductSettings:
    """
    Attributes:
        required (Union[Unset, bool]): If true, only institutions supporting this product will be available.
        prefetch (Union[Unset, bool]): If true, MoneyKit will begin preparing this data to make it available as soon as
            possible after linking even if `required` is false. If false, MoneyKit will prepare the data after the first
            manual data refresh.
        extend_history (Union[Unset, bool]): If this is set to true, we will attempt to get as much history as possible.
            This is not guaranteed to work for all institutions. By default at least 30 days is retrieved (although
            sometimes this can be more).
    """

    required: Union[Unset, bool] = False
    prefetch: Union[Unset, bool] = False
    extend_history: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        required = self.required
        prefetch = self.prefetch
        extend_history = self.extend_history

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required is not UNSET:
            field_dict["required"] = required
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch
        if extend_history is not UNSET:
            field_dict["extend_history"] = extend_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        required = d.pop("required", UNSET)

        prefetch = d.pop("prefetch", UNSET)

        extend_history = d.pop("extend_history", UNSET)

        transactions_product_settings = cls(
            required=required,
            prefetch=prefetch,
            extend_history=extend_history,
        )

        transactions_product_settings.additional_properties = d
        return transactions_product_settings

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
