from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.link_permission_scope import LinkPermissionScope

T = TypeVar("T", bound="RequestedLinkPermission")


@attr.s(auto_attribs=True)
class RequestedLinkPermission:
    """
    Attributes:
        scope (LinkPermissionScope): Permissions that a link has access to. These are accepted by a user.
        reason (str): The reason your app uses this data that will be displayed to the user.
        required (bool): If true, only institutions that support this data type will be available,
                    and the user **must** grant this permission or the link will not be created.  If false, then the
            available
                    institutions list may include those that do not support this data type, and even if the user declines to
                    grant this permission, the link will still be created (so long as at least one permission is granted).
    """

    scope: LinkPermissionScope
    reason: str
    required: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope.value

        reason = self.reason
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "reason": reason,
                "required": required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scope = LinkPermissionScope(d.pop("scope"))

        reason = d.pop("reason")

        required = d.pop("required")

        requested_link_permission = cls(
            scope=scope,
            reason=reason,
            required=required,
        )

        requested_link_permission.additional_properties = d
        return requested_link_permission

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
