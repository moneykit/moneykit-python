import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_app import CustomerApp


T = TypeVar("T", bound="IntrospectClientResponse")


@attr.s(auto_attribs=True)
class IntrospectClientResponse:
    """MoneyKit API client for an application.

    Example:
        {'client_id': 'production_5c739a369515e10fc9e0', 'client_name': 'My App (Prod)', 'scope': 'link_session:create
            link:data:read link:data:refresh institutions:read', 'app': {'id': '3d18cdd1-fa96-4423-b781-bd5be036830e',
            'app_name': 'My App'}}

    Attributes:
        client_id (str): Your application's MoneyKit client ID. Example: production_5c739a369515e10fc9e0.
        client_name (str): Friendly API client name for identification. Example: My App (Prod).
        scope (str): Actions allowed by the client.
        app (CustomerApp): Customer Application for a specific environment
        disabled_at (Union[Unset, None, datetime.datetime]): Set to timestamp if the client has been disabled.
    """

    client_id: str
    client_name: str
    scope: str
    app: "CustomerApp"
    disabled_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        client_id = self.client_id
        client_name = self.client_name
        scope = self.scope
        app = self.app.to_dict()

        disabled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.disabled_at, Unset):
            disabled_at = self.disabled_at.isoformat() if self.disabled_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_name": client_name,
                "scope": scope,
                "app": app,
            }
        )
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_app import CustomerApp

        d = src_dict.copy()
        client_id = d.pop("client_id")

        client_name = d.pop("client_name")

        scope = d.pop("scope")

        app = CustomerApp.from_dict(d.pop("app"))

        _disabled_at = d.pop("disabled_at", UNSET)
        disabled_at: Union[Unset, None, datetime.datetime]
        if _disabled_at is None:
            disabled_at = None
        elif isinstance(_disabled_at, Unset):
            disabled_at = UNSET
        else:
            disabled_at = isoparse(_disabled_at)

        introspect_client_response = cls(
            client_id=client_id,
            client_name=client_name,
            scope=scope,
            app=app,
            disabled_at=disabled_at,
        )

        introspect_client_response.additional_properties = d
        return introspect_client_response

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
