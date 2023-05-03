from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.link_session_error_invalid_token_exchange_error_code import LinkSessionErrorInvalidTokenExchangeErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSessionErrorInvalidTokenExchange")


@attr.s(auto_attribs=True)
class LinkSessionErrorInvalidTokenExchange:
    """
    Attributes:
        error_message (str): Error message Example: Invalid token for link.
        error_code (Union[Unset, LinkSessionErrorInvalidTokenExchangeErrorCode]):  Default:
            LinkSessionErrorInvalidTokenExchangeErrorCode.LINK_SESSION_ERROR_INVALID_TOKEN_EXCHANGE.
        documentation_url (Union[Unset, None, str]):
    """

    error_message: str
    error_code: Union[
        Unset, LinkSessionErrorInvalidTokenExchangeErrorCode
    ] = LinkSessionErrorInvalidTokenExchangeErrorCode.LINK_SESSION_ERROR_INVALID_TOKEN_EXCHANGE
    documentation_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_message = self.error_message
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_message": error_message,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_message = d.pop("error_message")

        _error_code = d.pop("error_code", UNSET)
        error_code: Union[Unset, LinkSessionErrorInvalidTokenExchangeErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = LinkSessionErrorInvalidTokenExchangeErrorCode(_error_code)

        documentation_url = d.pop("documentation_url", UNSET)

        link_session_error_invalid_token_exchange = cls(
            error_message=error_message,
            error_code=error_code,
            documentation_url=documentation_url,
        )

        link_session_error_invalid_token_exchange.additional_properties = d
        return link_session_error_invalid_token_exchange

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
