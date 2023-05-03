from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_error_rate_limit_exceeded_response_error_code import APIErrorRateLimitExceededResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIErrorRateLimitExceededResponse")


@attr.s(auto_attribs=True)
class APIErrorRateLimitExceededResponse:
    """
    Attributes:
        error_code (Union[Unset, APIErrorRateLimitExceededResponseErrorCode]):  Default:
            APIErrorRateLimitExceededResponseErrorCode.API_ERROR_RATE_LIMIT_EXCEEDED.
        error_message (Union[Unset, str]): Error message Default: 'Rate limit exceeded'.
        documentation_url (Union[Unset, None, str]):
    """

    error_code: Union[
        Unset, APIErrorRateLimitExceededResponseErrorCode
    ] = APIErrorRateLimitExceededResponseErrorCode.API_ERROR_RATE_LIMIT_EXCEEDED
    error_message: Union[Unset, str] = "Rate limit exceeded"
    documentation_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        error_message = self.error_message
        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _error_code = d.pop("error_code", UNSET)
        error_code: Union[Unset, APIErrorRateLimitExceededResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = APIErrorRateLimitExceededResponseErrorCode(_error_code)

        error_message = d.pop("error_message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        api_error_rate_limit_exceeded_response = cls(
            error_code=error_code,
            error_message=error_message,
            documentation_url=documentation_url,
        )

        api_error_rate_limit_exceeded_response.additional_properties = d
        return api_error_rate_limit_exceeded_response

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
