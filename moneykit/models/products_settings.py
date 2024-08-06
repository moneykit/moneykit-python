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
from moneykit.models.product_settings import ProductSettings
from moneykit.models.transactions_product_settings import TransactionsProductSettings

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ProductsSettings(BaseModel):
    """
    ProductsSettings
    """  # noqa: E501

    account_numbers: Optional[ProductSettings] = None
    identity: Optional[ProductSettings] = None
    transactions: Optional[TransactionsProductSettings] = None
    investments: Optional[ProductSettings] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "account_numbers",
        "identity",
        "transactions",
        "investments",
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
        """Create an instance of ProductsSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_numbers
        if self.account_numbers:
            _dict["account_numbers"] = self.account_numbers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict["identity"] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transactions
        if self.transactions:
            _dict["transactions"] = self.transactions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of investments
        if self.investments:
            _dict["investments"] = self.investments.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductsSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "account_numbers": ProductSettings.from_dict(obj.get("account_numbers"))
                if obj.get("account_numbers") is not None
                else None,
                "identity": ProductSettings.from_dict(obj.get("identity"))
                if obj.get("identity") is not None
                else None,
                "transactions": TransactionsProductSettings.from_dict(
                    obj.get("transactions")
                )
                if obj.get("transactions") is not None
                else None,
                "investments": ProductSettings.from_dict(obj.get("investments"))
                if obj.get("investments") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
