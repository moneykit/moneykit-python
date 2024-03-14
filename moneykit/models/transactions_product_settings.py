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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionsProductSettings(BaseModel):
    """
    TransactionsProductSettings
    """  # noqa: E501

    required: Optional[StrictBool] = Field(
        default=False,
        description="If true, only institutions supporting this product will be available.",
    )
    prefetch: Optional[StrictBool] = Field(
        default=False,
        description="If true, the data will be available as soon as possible after linking, even if `required` is false. If false, the data will be available after the first manual data refresh.",
    )
    reason: Optional[StrictStr] = Field(
        default=None,
        description='A **brief** description of the reason your app wants this data.         This description will follow the words "...data is used to", and will be displayed         to the user when permission is requested.  You should provide this field if your         app does not request this product by default, or if you want to show a particular         reason for requesting the product during this link session.',
    )
    extend_history: Optional[StrictBool] = Field(
        default=False,
        description="If true, MoneyKit will attempt to fetch as much transaction history as possible. Not all institutions supply the same extent of transaction history. Generally, however, at least the past 30 days of transactions are available.",
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "required",
        "prefetch",
        "reason",
        "extend_history",
    ]

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
        """Create an instance of TransactionsProductSettings from a JSON string"""
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
        """Create an instance of TransactionsProductSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "required": obj.get("required")
                if obj.get("required") is not None
                else False,
                "prefetch": obj.get("prefetch")
                if obj.get("prefetch") is not None
                else False,
                "reason": obj.get("reason"),
                "extend_history": obj.get("extend_history")
                if obj.get("extend_history") is not None
                else False,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
