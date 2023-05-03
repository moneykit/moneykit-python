from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.account_group import AccountGroup


T = TypeVar("T", bound="GetUserAccountsResponseLinks")


@attr.s(auto_attribs=True)
class GetUserAccountsResponseLinks:
    """The set of all accounts belonging to this user,
    as a dictionary of `{link_id:[accounts]}`.

    """

    additional_properties: Dict[str, "AccountGroup"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_group import AccountGroup

        d = src_dict.copy()
        get_user_accounts_response_links = cls()


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AccountGroup.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_user_accounts_response_links.additional_properties = additional_properties
        return get_user_accounts_response_links

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AccountGroup":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AccountGroup") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
