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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from moneykit.models.transaction_response import TransactionResponse

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class GetUserTransactionsResponse(BaseModel):
    """
    GetUserTransactionsResponse
    """  # noqa: E501

    total: StrictInt = Field(description="The total number of results for this query.")
    page: StrictInt = Field(
        description="The page number corresponding to this batch of results."
    )
    size: StrictInt = Field(description="The number of results in this batch.")
    transactions: List[TransactionResponse]
    accounts: Optional[Any]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "total",
        "page",
        "size",
        "transactions",
        "accounts",
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
        """Create an instance of GetUserTransactionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict["transactions"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if accounts (nullable) is None
        # and model_fields_set contains the field
        if self.accounts is None and "accounts" in self.model_fields_set:
            _dict["accounts"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetUserTransactionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "total": obj.get("total"),
                "page": obj.get("page"),
                "size": obj.get("size"),
                "transactions": [
                    TransactionResponse.from_dict(_item)
                    for _item in obj.get("transactions")
                ]
                if obj.get("transactions") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
