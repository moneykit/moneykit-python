from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.jwk_set_keys_item import JWKSetKeysItem


T = TypeVar("T", bound="JWKSet")


@attr.s(auto_attribs=True)
class JWKSet:
    """
    Example:
        {'keys': [{'crv': 'P-256', 'x': 'KqPQ0SAYk3Zkizuap0JP6r2XcdGKSaYBsVHJgyLyOnA', 'y':
            '627ZZERxpVBwpjpK5U2bVboOJ2AkI0Iz_J1kmYKl7Bc', 'kty': 'EC', 'alg': 'ES256', 'use': 'sig', 'kid':
            'xMtcLMEWp9GF-5A_COcTypt-tq9hkRa0oOfaruFF'}]}

    Attributes:
        keys (List['JWKSetKeysItem']): JWKs used for validating MoneyKit-issued tokens.
    """

    keys: List["JWKSetKeysItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()

            keys.append(keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jwk_set_keys_item import JWKSetKeysItem

        d = src_dict.copy()
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = JWKSetKeysItem.from_dict(keys_item_data)

            keys.append(keys_item)

        jwk_set = cls(
            keys=keys,
        )

        jwk_set.additional_properties = d
        return jwk_set

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
