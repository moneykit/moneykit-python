from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGenerateAccessTokenAuthTokenPost")


@attr.s(auto_attribs=True)
class BodyGenerateAccessTokenAuthTokenPost:
    """
    Attributes:
        grant_type (Union[Unset, None, str]): Token grant type. Only `client_credentials` supported.
        scope (Union[Unset, str]): Actions to be allowed for this token, given as one or more strings separated by
            spaces.
                        If omitted, all actions allowed for your application will be granted to this token. Default: ''.
        client_id (Union[Unset, None, str]): Your application's MoneyKit client ID.
        client_secret (Union[Unset, None, str]): Your application's MoneyKit client secret.
    """

    grant_type: Union[Unset, None, str] = UNSET
    scope: Union[Unset, str] = ""
    client_id: Union[Unset, None, str] = UNSET
    client_secret: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type
        scope = self.scope
        client_id = self.client_id
        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type", UNSET)

        scope = d.pop("scope", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        body_generate_access_token_auth_token_post = cls(
            grant_type=grant_type,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )

        body_generate_access_token_auth_token_post.additional_properties = d
        return body_generate_access_token_auth_token_post

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
