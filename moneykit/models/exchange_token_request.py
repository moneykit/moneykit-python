from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ExchangeTokenRequest")


@attr.s(auto_attribs=True)
class ExchangeTokenRequest:
    """
    Attributes:
        exchangeable_token (str): The token returned to your front end by MoneyLink's onSuccess callback. Example:
            c7318ff7-257c-490e-8242-03a815b223b7.
    """

    exchangeable_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exchangeable_token = self.exchangeable_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchangeable_token": exchangeable_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exchangeable_token = d.pop("exchangeable_token")

        exchange_token_request = cls(
            exchangeable_token=exchangeable_token,
        )

        exchange_token_request.additional_properties = d
        return exchange_token_request

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
