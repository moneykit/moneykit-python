from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.link_common import LinkCommon


T = TypeVar("T", bound="ExchangeTokenResponse")


@attr.s(auto_attribs=True)
class ExchangeTokenResponse:
    """
    Attributes:
        link_id (str): The unique ID associated with this link. Example: c7318ff7-257c-490e-8242-03a815b223b7.
        link (LinkCommon):  Example: {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase',
            'institution_name': 'Chase', 'provider': 'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11',
            'tags': ['user_type:admin'], 'products': {'accounts': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11'}, 'identity': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required': True, 'prefetch': False}}}}.
    """

    link_id: str
    link: "LinkCommon"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_id = self.link_id
        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link_id": link_id,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_common import LinkCommon

        d = src_dict.copy()
        link_id = d.pop("link_id")

        link = LinkCommon.from_dict(d.pop("link"))

        exchange_token_response = cls(
            link_id=link_id,
            link=link,
        )

        exchange_token_response.additional_properties = d
        return exchange_token_response

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
