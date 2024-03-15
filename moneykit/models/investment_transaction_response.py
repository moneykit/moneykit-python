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
from pydantic import BaseModel, StrictStr
from pydantic import Field

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class InvestmentTransactionResponse(BaseModel):
    """
    InvestmentTransactionResponse
    """  # noqa: E501

    investment_transaction_id: StrictStr = Field(
        description="The unique ID for this investment transaction."
    )
    account_id: StrictStr = Field(
        description="The ID of the account in which this investment transaction occurred."
    )
    amount: StrictStr = Field(
        description="The total value of this transaction, denominated in account currency.  Positive values indicate         debits (deposits); negative values are credits (withdrawals).  For example, for a `buy` transaction, the amount         will be equal to `-(quantity * price + fees)`."
    )
    var_date: date = Field(
        description="The effective (posted) date of the transaction, in ISO-8601 format.",
        alias="date",
    )
    datetime_: Optional[datetime] = Field(
        alias="datetime",
        default=None,
        description="If the institution has provided the actual time of the transaction, this field             contains the full date and time of the transaction, in ISO-8601 format.  If the time is             not available, this field will be null.             <p>Note that the time is generally reported in the timezone of the institution or the account holder.",
    )
    description: StrictStr = Field(
        description="A normalized, cleaned transaction description suitable for presentation to the end user."
    )
    type: StrictStr = Field(
        description="The type of transaction (buy, sell, cash, fee, transfer).  May include a dotted subtype,         for example, `buy.buy_to_cover` or `fee.transfer_fee`."
    )
    fees: Optional[StrictStr] = Field(
        default=None,
        description="The combined value of any fees applied to the transaction.  Fees are subtracted from the         total transaction amount, and are reported as positive values; refunds are reported as negative values.",
    )
    forex_rate: Optional[StrictStr] = Field(
        default=None,
        description="The currency exchange rate applied.  Only present for transactions involving a security that is         denominated in a currency other than the account currency.",
    )
    price: Optional[StrictStr] = Field(
        default=None,
        description="The price per share, denominated in account currency.  Omitted for transactions not involving         a security.",
    )
    quantity: Optional[StrictStr] = Field(
        default=None,
        description='The units of security (aka "shares") bought, sold, or transferred.  Omitted for transactions         not involving a security.  Positive values indicate shares added to the account.',
    )
    security_id: Optional[StrictStr] = Field(
        default=None,
        description="The MoneyKit ID of the security involved in this transaction (for example, the security bought         or sold, or upon which interest or dividends are paid.",
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "investment_transaction_id",
        "account_id",
        "amount",
        "date",
        "datetime",
        "description",
        "type",
        "fees",
        "forex_rate",
        "price",
        "quantity",
        "security_id",
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
        """Create an instance of InvestmentTransactionResponse from a JSON string"""
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
        """Create an instance of InvestmentTransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "investment_transaction_id": obj.get("investment_transaction_id"),
                "account_id": obj.get("account_id"),
                "amount": obj.get("amount"),
                "date": obj.get("date"),
                "datetime": obj.get("datetime"),
                "description": obj.get("description"),
                "type": obj.get("type"),
                "fees": obj.get("fees"),
                "forex_rate": obj.get("forex_rate"),
                "price": obj.get("price"),
                "quantity": obj.get("quantity"),
                "security_id": obj.get("security_id"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
