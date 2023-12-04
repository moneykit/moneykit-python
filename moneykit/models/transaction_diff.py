# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from moneykit.models.transaction import Transaction

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionDiff(BaseModel):
    """
    TransactionDiff
    """  # noqa: E501

    created: List[Transaction]
    updated: List[Transaction]
    removed: List[StrictStr]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["created", "updated", "removed"]

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
        """Create an instance of TransactionDiff from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in created (list)
        _items = []
        if self.created:
            for _item in self.created:
                if _item:
                    _items.append(_item.to_dict())
            _dict["created"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in updated (list)
        _items = []
        if self.updated:
            for _item in self.updated:
                if _item:
                    _items.append(_item.to_dict())
            _dict["updated"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TransactionDiff from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created": [
                    Transaction.from_dict(_item) for _item in obj.get("created")
                ]
                if obj.get("created") is not None
                else None,
                "updated": [
                    Transaction.from_dict(_item) for _item in obj.get("updated")
                ]
                if obj.get("updated") is not None
                else None,
                "removed": obj.get("removed"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj