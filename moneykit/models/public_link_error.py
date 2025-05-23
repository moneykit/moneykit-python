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


class PublicLinkError(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    SYSTEM_ERROR = "system_error"
    PROVIDER_ERROR = "provider_error"
    INSTITUTION_ERROR = "institution_error"
    USER_ERROR = "user_error"
    AUTH_EXPIRED = "auth_expired"
    NO_ACCOUNTS = "no_accounts"
    USER_SETUP_REQUIRED = "user_setup_required"
    INVALID_CREDENTIALS = "invalid_credentials"
    USER_OAUTH_DENIED = "user_oauth_denied"
    USER_INPUT_INCORRECT = "user_input_incorrect"
    INCOMPLETE = "incomplete"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PublicLinkError from a JSON string"""
        return cls(json.loads(json_str))
