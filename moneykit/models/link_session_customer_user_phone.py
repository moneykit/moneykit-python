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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
from moneykit.models.country import Country

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class LinkSessionCustomerUserPhone(BaseModel):
    """
    LinkSessionCustomerUserPhone
    """  # noqa: E501

    number: Annotated[str, Field(min_length=4, strict=True, max_length=250)] = Field(
        description="The user's phone number, preferably in E164 format, including the country code."
    )
    country: Optional[Country] = None
    customer_verified_at: Optional[datetime] = Field(
        default=None,
        description="Optional timestamp that marks when you last verified this number (such as when the user most         recently returned a verification code sent via SMS to this number).         Only include this field if you verified the number.  You may supply zeros if the time (but not the date)         is unknown.",
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["number", "country", "customer_verified_at"]

    @field_validator("number")
    def number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+?[ 0-9()\.#]+$", value):
            raise ValueError(
                r"must validate the regular expression /^\+?[ 0-9()\.#]+$/"
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
        """Create an instance of LinkSessionCustomerUserPhone from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LinkSessionCustomerUserPhone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "number": obj.get("number"),
                "country": obj.get("country"),
                "customer_verified_at": obj.get("customer_verified_at"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
