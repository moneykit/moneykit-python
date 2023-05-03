from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_user_links_response_links import GetUserLinksResponseLinks


T = TypeVar("T", bound="GetUserLinksResponse")


@attr.s(auto_attribs=True)
class GetUserLinksResponse:
    """
    Example:
        {'links': {'mk_eqkWN34UEoa2NxyALG8pcV': {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase',
            'institution_name': 'Chase', 'provider': 'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11',
            'tags': ['user_type:admin'], 'products': {'accounts': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11'}, 'identity': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required': True, 'prefetch': False}}}}}}

    Attributes:
        links (GetUserLinksResponseLinks): The set of links belonging to this user, as a dictionary
                    of `{link_id:link}`.
    """

    links: "GetUserLinksResponseLinks"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_user_links_response_links import GetUserLinksResponseLinks

        d = src_dict.copy()
        links = GetUserLinksResponseLinks.from_dict(d.pop("links"))

        get_user_links_response = cls(
            links=links,
        )

        get_user_links_response.additional_properties = d
        return get_user_links_response

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
