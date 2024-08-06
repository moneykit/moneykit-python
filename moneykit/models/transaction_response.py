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

from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from moneykit.models.transaction_enrichment_response import (
    TransactionEnrichmentResponse,
)
from moneykit.models.transaction_type import TransactionType

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionResponse(BaseModel):
    """
    TransactionResponse
    """  # noqa: E501

    transaction_id: StrictStr = Field(description="The unique ID for this transaction.")
    account_id: StrictStr = Field(
        description="The ID of the account in which this transaction occurred."
    )
    amount: StrictStr = Field(
        description="The amount of this transaction, denominated in account currency.  This amount is always         non-negative.  The `type` field indicates whether it is entering or leaving the account."
    )
    type: TransactionType
    currency: StrictStr = Field(
        description="The ISO-4217 currency code of the transaction."
    )
    date_: date = Field(
        description="The effective (posted) date of the transaction, in ISO-8601 format.  For pending transactions,             this date is when the transaction was initiated.",
        alias="date",
    )
    datetime_: Optional[datetime] = Field(
        alias="datetime",
        default=None,
        description="If the institution has provided the actual time of the transaction, this field             contains the full date and time of the transaction, in ISO-8601 format.  If the time is             not available, this field will be null.             <p>Note that the time is generally reported in the timezone of the institution or the account holder.",
    )
    description: Optional[StrictStr] = Field(
        default=None,
        description="A normalized, cleaned transaction description suitable for presentation to the end user.             Commonly this will be the merchant or counterparty name.",
    )
    raw_description: Optional[StrictStr] = Field(
        default=None,
        description="The raw transaction description as provided by the institution, where available.",
    )
    pending: StrictBool = Field(
        description="If true, this transaction is pending or unsettled and has not yet affected the account.         Commonly these are credit card transactions, particularly approvals (holds) such as for hotel or restaurant         reservations placed in advance where the final amount is still to be determined."
    )
    category: Optional[StrictStr] = Field(
        default=None, description="(deprecated) Refer to enrichment.category."
    )
    enrichment: Optional[TransactionEnrichmentResponse] = None
    original_id: Optional[StrictStr] = Field(
        default=None,
        description="The original ID of this transaction, if supplied (by you) during an import.",
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "transaction_id",
        "account_id",
        "amount",
        "type",
        "currency",
        "date",
        "datetime",
        "description",
        "raw_description",
        "pending",
        "category",
        "enrichment",
        "original_id",
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
        """Create an instance of TransactionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of enrichment
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "transaction_id": obj.get("transaction_id"),
                "account_id": obj.get("account_id"),
                "amount": obj.get("amount"),
                "type": obj.get("type"),
                "currency": obj.get("currency"),
                "date": obj.get("date"),
                "datetime": obj.get("datetime"),
                "description": obj.get("description"),
                "raw_description": obj.get("raw_description"),
                "pending": obj.get("pending"),
                "category": obj.get("category"),
                "enrichment": TransactionEnrichmentResponse.from_dict(
                    obj.get("enrichment")
                )
                if obj.get("enrichment") is not None
                else None,
                "original_id": obj.get("original_id"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
