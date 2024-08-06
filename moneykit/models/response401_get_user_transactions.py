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
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, ValidationError, field_validator
from moneykit.models.api_error_auth_expired_access_token_response import (
    APIErrorAuthExpiredAccessTokenResponse,
)
from moneykit.models.api_error_auth_unauthorized_response import (
    APIErrorAuthUnauthorizedResponse,
)
from typing import Union, Any, List, TYPE_CHECKING, Dict
from typing_extensions import Literal

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

RESPONSE401GETUSERTRANSACTIONS_ANY_OF_SCHEMAS = [
    "APIErrorAuthExpiredAccessTokenResponse",
    "APIErrorAuthUnauthorizedResponse",
]


class Response401GetUserTransactions(BaseModel):
    """
    Response401GetUserTransactions
    """

    # data type: APIErrorAuthExpiredAccessTokenResponse
    anyof_schema_1_validator: Optional[APIErrorAuthExpiredAccessTokenResponse] = None
    # data type: APIErrorAuthUnauthorizedResponse
    anyof_schema_2_validator: Optional[APIErrorAuthUnauthorizedResponse] = None
    if TYPE_CHECKING:
        actual_instance: Optional[
            Union[
                APIErrorAuthExpiredAccessTokenResponse, APIErrorAuthUnauthorizedResponse
            ]
        ] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[RESPONSE401GETUSERTRANSACTIONS_ANY_OF_SCHEMAS]

    model_config = {"validate_assignment": True}

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        instance = Response401GetUserTransactions.model_construct()
        error_messages = []
        # validate data type: APIErrorAuthExpiredAccessTokenResponse
        if not isinstance(v, APIErrorAuthExpiredAccessTokenResponse):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `APIErrorAuthExpiredAccessTokenResponse`"
            )
        else:
            return v

        # validate data type: APIErrorAuthUnauthorizedResponse
        if not isinstance(v, APIErrorAuthUnauthorizedResponse):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `APIErrorAuthUnauthorizedResponse`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in Response401GetUserTransactions with anyOf schemas: APIErrorAuthExpiredAccessTokenResponse, APIErrorAuthUnauthorizedResponse. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[APIErrorAuthExpiredAccessTokenResponse] = None
        try:
            instance.actual_instance = APIErrorAuthExpiredAccessTokenResponse.from_json(
                json_str
            )
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[APIErrorAuthUnauthorizedResponse] = None
        try:
            instance.actual_instance = APIErrorAuthUnauthorizedResponse.from_json(
                json_str
            )
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into Response401GetUserTransactions with anyOf schemas: APIErrorAuthExpiredAccessTokenResponse, APIErrorAuthUnauthorizedResponse. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
