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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from moneykit.models.ach_number import AchNumber
from moneykit.models.bacs_number import BacsNumber
from moneykit.models.eft_number import EftNumber
from moneykit.models.international_number import InternationalNumber

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccountNumbersLegacy20230218(BaseModel):
    """
    AccountNumbersLegacy20230218
    """  # noqa: E501

    ach: List[AchNumber]
    bacs: List[BacsNumber]
    eft: List[EftNumber]
    international: List[InternationalNumber]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["ach", "bacs", "eft", "international"]

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
        """Create an instance of AccountNumbersLegacy20230218 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ach (list)
        _items = []
        if self.ach:
            for _item in self.ach:
                if _item:
                    _items.append(_item.to_dict())
            _dict["ach"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bacs (list)
        _items = []
        if self.bacs:
            for _item in self.bacs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["bacs"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in eft (list)
        _items = []
        if self.eft:
            for _item in self.eft:
                if _item:
                    _items.append(_item.to_dict())
            _dict["eft"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in international (list)
        _items = []
        if self.international:
            for _item in self.international:
                if _item:
                    _items.append(_item.to_dict())
            _dict["international"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountNumbersLegacy20230218 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ach": [AchNumber.from_dict(_item) for _item in obj.get("ach")]
                if obj.get("ach") is not None
                else None,
                "bacs": [BacsNumber.from_dict(_item) for _item in obj.get("bacs")]
                if obj.get("bacs") is not None
                else None,
                "eft": [EftNumber.from_dict(_item) for _item in obj.get("eft")]
                if obj.get("eft") is not None
                else None,
                "international": [
                    InternationalNumber.from_dict(_item)
                    for _item in obj.get("international")
                ]
                if obj.get("international") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
