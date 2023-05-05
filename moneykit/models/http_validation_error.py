from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.http_validation_error_error_code import HTTPValidationErrorErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


T = TypeVar("T", bound="HTTPValidationError")


@attr.s(auto_attribs=True)
class HTTPValidationError:
    """
    Attributes:
        validation_errors (List['ValidationError']):
        error_code (Union[Unset, HTTPValidationErrorErrorCode]):  Default:
            HTTPValidationErrorErrorCode.API_ERROR_REQUEST_VALIDATION_FAILED.
        error_message (Union[Unset, str]): Error message Default: 'Request validation error'.
        documentation_url (Union[Unset, None, str]):
    """

    validation_errors: List["ValidationError"]
    error_code: Union[
        Unset, HTTPValidationErrorErrorCode
    ] = HTTPValidationErrorErrorCode.API_ERROR_REQUEST_VALIDATION_FAILED
    error_message: Union[Unset, str] = "Request validation error"
    documentation_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validation_errors = []
        for validation_errors_item_data in self.validation_errors:
            validation_errors_item = validation_errors_item_data.to_dict()

            validation_errors.append(validation_errors_item)

        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        error_message = self.error_message
        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "validation_errors": validation_errors,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_error import ValidationError

        d = src_dict.copy()
        validation_errors = []
        _validation_errors = d.pop("validation_errors")
        for validation_errors_item_data in _validation_errors:
            validation_errors_item = ValidationError.from_dict(validation_errors_item_data)

            validation_errors.append(validation_errors_item)

        _error_code = d.pop("error_code", UNSET)
        error_code: Union[Unset, HTTPValidationErrorErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = HTTPValidationErrorErrorCode(_error_code)

        error_message = d.pop("error_message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        http_validation_error = cls(
            validation_errors=validation_errors,
            error_code=error_code,
            error_message=error_message,
            documentation_url=documentation_url,
        )

        http_validation_error.additional_properties = d
        return http_validation_error

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
