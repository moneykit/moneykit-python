# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Product(str, Enum):
    """
    Features that a route supports
    """

    """
    allowed enum values
    """
    ACCOUNTS = "accounts"
    ACCOUNT_NUMBERS = "account_numbers"
    IDENTITY = "identity"
    TRANSACTIONS = "transactions"
    INVESTMENTS = "investments"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Product from a JSON string"""
        return cls(json.loads(json_str))
