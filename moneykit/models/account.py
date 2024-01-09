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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from moneykit.models.account_balances import AccountBalances

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Account(BaseModel):
    """
    Account
    """  # noqa: E501

    account_id: StrictStr = Field(
        description="MoneyKit's unique ID for the account.         <p>The `account_id` is distinct from the institution's account number.  For accounts that may change account         numbers from time to time, such as credit cards, MoneyKit attempts to keep the `account_id` constant.         However, if MoneyKit can't reconcile the new account data with the old data, the `account_id` may change."
    )
    account_type: StrictStr = Field(
        description="See <a href=/pages/account_types>Account Types</a> for an explanation of account types.  Account types are         dot-prefixed with one of `depository`, `investment`, `liability`, or `other`; or the value is `unknown`.         <p>**Balances for `liability` accounts are reversed:**  negative balances (the amount owed) are reported as         positive values.  For all other types of accounts, a negative balance indicates the amount owed."
    )
    name: StrictStr = Field(
        description="The account name, according to the institution.  Note that some institutions allow         the end user to nickname the account; in such cases this field may be the name assigned by the user."
    )
    account_mask: Optional[StrictStr] = Field(
        default=None,
        description="The last four characters (usually digits) of the account number.         Note that this mask may be non-unique between accounts.",
    )
    balances: AccountBalances
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "account_id",
        "account_type",
        "name",
        "account_mask",
        "balances",
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
        """Create an instance of Account from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of balances
        if self.balances:
            _dict["balances"] = self.balances.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "account_id": obj.get("account_id"),
                "account_type": obj.get("account_type"),
                "name": obj.get("name"),
                "account_mask": obj.get("account_mask"),
                "balances": AccountBalances.from_dict(obj.get("balances"))
                if obj.get("balances") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
