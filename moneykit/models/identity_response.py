from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.account_identity import AccountIdentity
    from ..models.link_common import LinkCommon


T = TypeVar("T", bound="IdentityResponse")


@attr.s(auto_attribs=True)
class IdentityResponse:
    """
    Attributes:
        accounts (List['AccountIdentity']): A list of accounts associated with the link.
        link (LinkCommon):  Example: {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase',
            'institution_name': 'Chase', 'provider': 'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11',
            'tags': ['user_type:admin'], 'products': {'accounts': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11'}, 'identity': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required': True, 'prefetch': False}}}}.
    """

    accounts: List["AccountIdentity"]
    link: "LinkCommon"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()

            accounts.append(accounts_item)

        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_identity import AccountIdentity
        from ..models.link_common import LinkCommon

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = AccountIdentity.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        link = LinkCommon.from_dict(d.pop("link"))

        identity_response = cls(
            accounts=accounts,
            link=link,
        )

        identity_response.additional_properties = d
        return identity_response

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
