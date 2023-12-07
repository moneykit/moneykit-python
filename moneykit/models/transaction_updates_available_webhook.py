# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionUpdatesAvailableWebhook(BaseModel):
    """
    TransactionUpdatesAvailableWebhook
    """  # noqa: E501

    webhook_event: Literal[
        "transactions.updates_available"
    ] = "transactions.updates_available"
    webhook_major_version: int = 1
    webhook_minor_version: int = 0
    webhook_idempotency_key: StrictStr
    webhook_timestamp: datetime
    link_id: StrictStr
    has_history: StrictBool
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "webhook_event",
        "webhook_major_version",
        "webhook_minor_version",
        "webhook_idempotency_key",
        "webhook_timestamp",
        "link_id",
        "has_history",
    ]

    @field_validator("webhook_event")
    def webhook_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("transactions.updates_available",):
            raise ValueError(
                "must be one of enum values ('transactions.updates_available')"
            )
        return value

    @field_validator("webhook_major_version")
    def webhook_major_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (1,):
            raise ValueError("must be one of enum values (1)")
        return value

    @field_validator("webhook_minor_version")
    def webhook_minor_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0,):
            raise ValueError("must be one of enum values (0)")
        return value

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
        """Create an instance of TransactionUpdatesAvailableWebhook from a JSON string"""
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
        """Create an instance of TransactionUpdatesAvailableWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "webhook_event": obj.get("webhook_event")
                if obj.get("webhook_event") is not None
                else "transactions.updates_available",
                "webhook_major_version": obj.get("webhook_major_version")
                if obj.get("webhook_major_version") is not None
                else 1,
                "webhook_minor_version": obj.get("webhook_minor_version")
                if obj.get("webhook_minor_version") is not None
                else 0,
                "webhook_idempotency_key": obj.get("webhook_idempotency_key"),
                "webhook_timestamp": obj.get("webhook_timestamp"),
                "link_id": obj.get("link_id"),
                "has_history": obj.get("has_history"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
