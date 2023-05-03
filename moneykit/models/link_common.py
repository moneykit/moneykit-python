import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.link_error import LinkError
from ..models.link_state import LinkState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_products import LinkProducts


T = TypeVar("T", bound="LinkCommon")


@attr.s(auto_attribs=True)
class LinkCommon:
    """
    Example:
        {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase', 'institution_name': 'Chase', 'provider':
            'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11', 'tags': ['user_type:admin'], 'products':
            {'accounts': {'refreshed_at': '2023-02-16T09:14:11', 'last_attempted_at': '2023-02-16T09:14:11'}, 'identity':
            {'refreshed_at': '2023-02-16T09:14:11', 'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required':
            True, 'prefetch': False}}}}

    Attributes:
        link_id (str): The unique ID for this link. Example: mk_eqkWN34UEoa2NxyALG8pcV.
        institution_id (str): The unique ID for the institution this link is connected to. Example: chase.
        institution_name (str): The institution name this link is connected to. Example: Chase.
        state (LinkState): An enumeration.
        products (LinkProducts):
        error_code (Union[Unset, None, LinkError]): An enumeration.
        last_synced_at (Union[Unset, None, datetime.datetime]): An ISO-8601 timestamp indicating the last time that the
            account was updated. Example: 2023-02-16T09:14:11.
        tags (Union[Unset, None, List[str]]): Arbitrary strings used to describe this link. Example: ['smoke_test',
            'user_type:admin'].
    """

    link_id: str
    institution_id: str
    institution_name: str
    state: LinkState
    products: "LinkProducts"
    error_code: Union[Unset, None, LinkError] = UNSET
    last_synced_at: Union[Unset, None, datetime.datetime] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        link_id = self.link_id
        institution_id = self.institution_id
        institution_name = self.institution_name
        state = self.state.value

        products = self.products.to_dict()

        error_code: Union[Unset, None, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value if self.error_code else None

        last_synced_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat() if self.last_synced_at else None

        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link_id": link_id,
                "institution_id": institution_id,
                "institution_name": institution_name,
                "state": state,
                "products": products,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_products import LinkProducts

        d = src_dict.copy()
        link_id = d.pop("link_id")

        institution_id = d.pop("institution_id")

        institution_name = d.pop("institution_name")

        state = LinkState(d.pop("state"))

        products = LinkProducts.from_dict(d.pop("products"))

        _error_code = d.pop("error_code", UNSET)
        error_code: Union[Unset, None, LinkError]
        if _error_code is None:
            error_code = None
        elif isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = LinkError(_error_code)

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: Union[Unset, None, datetime.datetime]
        if _last_synced_at is None:
            last_synced_at = None
        elif isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = isoparse(_last_synced_at)

        tags = cast(List[str], d.pop("tags", UNSET))

        link_common = cls(
            link_id=link_id,
            institution_id=institution_id,
            institution_name=institution_name,
            state=state,
            products=products,
            error_code=error_code,
            last_synced_at=last_synced_at,
            tags=tags,
        )

        link_common.additional_properties = d
        return link_common

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
