# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from moneykit.models.validation_error import ValidationError

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class HTTPValidationError(BaseModel):
    """
    HTTPValidationError
    """  # noqa: E501

    error_code: Optional[StrictStr] = "api_error.request.validation_failed"
    error_message: Optional[StrictStr] = Field(
        default="Request validation error", description="Error message"
    )
    documentation_url: Optional[StrictStr] = None
    validation_errors: List[ValidationError]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "error_code",
        "error_message",
        "documentation_url",
        "validation_errors",
    ]

    @field_validator("error_code")
    def error_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("api_error.request.validation_failed",):
            raise ValueError(
                "must be one of enum values ('api_error.request.validation_failed')"
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HTTPValidationError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in validation_errors (list)
        _items = []
        if self.validation_errors:
            for _item in self.validation_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["validation_errors"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HTTPValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "error_code": obj.get("error_code")
                if obj.get("error_code") is not None
                else "api_error.request.validation_failed",
                "error_message": obj.get("error_message")
                if obj.get("error_message") is not None
                else "Request validation error",
                "documentation_url": obj.get("documentation_url"),
                "validation_errors": [
                    ValidationError.from_dict(_item)
                    for _item in obj.get("validation_errors")
                ]
                if obj.get("validation_errors") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
