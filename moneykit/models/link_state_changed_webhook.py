import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.link_error import LinkError
from ..models.link_state import LinkState
from ..models.link_state_changed_webhook_webhook_event import LinkStateChangedWebhookWebhookEvent
from ..models.link_state_changed_webhook_webhook_major_version import LinkStateChangedWebhookWebhookMajorVersion
from ..models.link_state_changed_webhook_webhook_minor_version import LinkStateChangedWebhookWebhookMinorVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkStateChangedWebhook")


@attr.s(auto_attribs=True)
class LinkStateChangedWebhook:
    """
    Attributes:
        webhook_idempotency_key (str):
        webhook_timestamp (datetime.datetime):
        link_id (str):
        link_tags (List[str]):
        state (LinkState): An enumeration.
        webhook_event (Union[Unset, LinkStateChangedWebhookWebhookEvent]):  Default:
            LinkStateChangedWebhookWebhookEvent.LINK_STATE_CHANGED.
        webhook_major_version (Union[Unset, LinkStateChangedWebhookWebhookMajorVersion]):  Default:
            LinkStateChangedWebhookWebhookMajorVersion.VALUE_1.
        webhook_minor_version (Union[Unset, LinkStateChangedWebhookWebhookMinorVersion]):  Default:
            LinkStateChangedWebhookWebhookMinorVersion.VALUE_0.
        error (Union[Unset, LinkError]): An enumeration.
        error_message (Union[Unset, None, str]):
    """

    webhook_idempotency_key: str
    webhook_timestamp: datetime.datetime
    link_id: str
    link_tags: List[str]
    state: LinkState
    webhook_event: Union[
        Unset, LinkStateChangedWebhookWebhookEvent
    ] = LinkStateChangedWebhookWebhookEvent.LINK_STATE_CHANGED
    webhook_major_version: Union[
        Unset, LinkStateChangedWebhookWebhookMajorVersion
    ] = LinkStateChangedWebhookWebhookMajorVersion.VALUE_1
    webhook_minor_version: Union[
        Unset, LinkStateChangedWebhookWebhookMinorVersion
    ] = LinkStateChangedWebhookWebhookMinorVersion.VALUE_0
    error: Union[Unset, LinkError] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook_idempotency_key = self.webhook_idempotency_key
        webhook_timestamp = self.webhook_timestamp.isoformat()

        link_id = self.link_id
        link_tags = self.link_tags

        state = self.state.value

        webhook_event: Union[Unset, str] = UNSET
        if not isinstance(self.webhook_event, Unset):
            webhook_event = self.webhook_event.value

        webhook_major_version: Union[Unset, int] = UNSET
        if not isinstance(self.webhook_major_version, Unset):
            webhook_major_version = self.webhook_major_version.value

        webhook_minor_version: Union[Unset, int] = UNSET
        if not isinstance(self.webhook_minor_version, Unset):
            webhook_minor_version = self.webhook_minor_version.value

        error: Union[Unset, str] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook_idempotency_key": webhook_idempotency_key,
                "webhook_timestamp": webhook_timestamp,
                "link_id": link_id,
                "link_tags": link_tags,
                "state": state,
            }
        )
        if webhook_event is not UNSET:
            field_dict["webhook_event"] = webhook_event
        if webhook_major_version is not UNSET:
            field_dict["webhook_major_version"] = webhook_major_version
        if webhook_minor_version is not UNSET:
            field_dict["webhook_minor_version"] = webhook_minor_version
        if error is not UNSET:
            field_dict["error"] = error
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook_idempotency_key = d.pop("webhook_idempotency_key")

        webhook_timestamp = isoparse(d.pop("webhook_timestamp"))

        link_id = d.pop("link_id")

        link_tags = cast(List[str], d.pop("link_tags"))

        state = LinkState(d.pop("state"))

        _webhook_event = d.pop("webhook_event", UNSET)
        webhook_event: Union[Unset, LinkStateChangedWebhookWebhookEvent]
        if isinstance(_webhook_event, Unset):
            webhook_event = UNSET
        else:
            webhook_event = LinkStateChangedWebhookWebhookEvent(_webhook_event)

        _webhook_major_version = d.pop("webhook_major_version", UNSET)
        webhook_major_version: Union[Unset, LinkStateChangedWebhookWebhookMajorVersion]
        if isinstance(_webhook_major_version, Unset):
            webhook_major_version = UNSET
        else:
            webhook_major_version = LinkStateChangedWebhookWebhookMajorVersion(_webhook_major_version)

        _webhook_minor_version = d.pop("webhook_minor_version", UNSET)
        webhook_minor_version: Union[Unset, LinkStateChangedWebhookWebhookMinorVersion]
        if isinstance(_webhook_minor_version, Unset):
            webhook_minor_version = UNSET
        else:
            webhook_minor_version = LinkStateChangedWebhookWebhookMinorVersion(_webhook_minor_version)

        _error = d.pop("error", UNSET)
        error: Union[Unset, LinkError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = LinkError(_error)

        error_message = d.pop("error_message", UNSET)

        link_state_changed_webhook = cls(
            webhook_idempotency_key=webhook_idempotency_key,
            webhook_timestamp=webhook_timestamp,
            link_id=link_id,
            link_tags=link_tags,
            state=state,
            webhook_event=webhook_event,
            webhook_major_version=webhook_major_version,
            webhook_minor_version=webhook_minor_version,
            error=error,
            error_message=error_message,
        )

        link_state_changed_webhook.additional_properties = d
        return link_state_changed_webhook

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
