from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.requested_link_permission import RequestedLinkPermission


T = TypeVar("T", bound="LinkPermissions")


@attr.s(auto_attribs=True)
class LinkPermissions:
    """
    Attributes:
        requested (List['RequestedLinkPermission']):
    """

    requested: List["RequestedLinkPermission"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requested = []
        for requested_item_data in self.requested:
            requested_item = requested_item_data.to_dict()

            requested.append(requested_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested": requested,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.requested_link_permission import RequestedLinkPermission

        d = src_dict.copy()
        requested = []
        _requested = d.pop("requested")
        for requested_item_data in _requested:
            requested_item = RequestedLinkPermission.from_dict(requested_item_data)

            requested.append(requested_item)

        link_permissions = cls(
            requested=requested,
        )

        link_permissions.additional_properties = d
        return link_permissions

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
