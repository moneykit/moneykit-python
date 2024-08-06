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
from pydantic import BaseModel
from moneykit.models.transaction_category_response import TransactionCategoryResponse
from moneykit.models.transaction_merchant_response import TransactionMerchantResponse
from moneykit.models.transaction_processor_response import TransactionProcessorResponse
from moneykit.models.transaction_recurrence_response import (
    TransactionRecurrenceResponse,
)
from moneykit.models.transaction_subcategory_response import (
    TransactionSubcategoryResponse,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionEnrichmentResponse(BaseModel):
    """
    TransactionEnrichmentResponse
    """  # noqa: E501

    category: TransactionCategoryResponse
    subcategory: Optional[TransactionSubcategoryResponse] = None
    merchant: Optional[TransactionMerchantResponse] = None
    processor: Optional[TransactionProcessorResponse] = None
    recurrence: Optional[TransactionRecurrenceResponse] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "category",
        "subcategory",
        "merchant",
        "processor",
        "recurrence",
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
        """Create an instance of TransactionEnrichmentResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict["category"] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subcategory
        if self.subcategory:
            _dict["subcategory"] = self.subcategory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of processor
        if self.processor:
            _dict["processor"] = self.processor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recurrence
        if self.recurrence:
            _dict["recurrence"] = self.recurrence.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TransactionEnrichmentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "category": TransactionCategoryResponse.from_dict(obj.get("category"))
                if obj.get("category") is not None
                else None,
                "subcategory": TransactionSubcategoryResponse.from_dict(
                    obj.get("subcategory")
                )
                if obj.get("subcategory") is not None
                else None,
                "merchant": TransactionMerchantResponse.from_dict(obj.get("merchant"))
                if obj.get("merchant") is not None
                else None,
                "processor": TransactionProcessorResponse.from_dict(
                    obj.get("processor")
                )
                if obj.get("processor") is not None
                else None,
                "recurrence": TransactionRecurrenceResponse.from_dict(
                    obj.get("recurrence")
                )
                if obj.get("recurrence") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
