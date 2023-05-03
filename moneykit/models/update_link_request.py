from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLinkRequest")


@attr.s(auto_attribs=True)
class UpdateLinkRequest:
    """
    Attributes:
        webhook (Union[Unset, None, str]): Sets the webhook URL for this link.
                    To remove a webhook for this link, set to `null`. Example: https://example.com/updated/hook.
        tags (Union[Unset, None, List[str]]): Arbitrary strings used to describe this link. Example: ['smoke_test',
            'user_type:admin'].
    """

    webhook: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook = self.webhook
        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook = d.pop("webhook", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        update_link_request = cls(
            webhook=webhook,
            tags=tags,
        )

        update_link_request.additional_properties = d
        return update_link_request

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
