# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
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
from typing_extensions import Annotated
from moneykit.models.link_session_customer_user import LinkSessionCustomerUser
from moneykit.models.link_session_setting_overrides import LinkSessionSettingOverrides
from moneykit.models.money_kit_connect_features import MoneyKitConnectFeatures

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CreateLinkSessionRequest(BaseModel):
    """
    CreateLinkSessionRequest
    """  # noqa: E501

    settings: Optional[LinkSessionSettingOverrides] = None
    customer_user: LinkSessionCustomerUser
    existing_link_id: Optional[StrictStr] = Field(
        default=None,
        description="Supply the existing `link_id` if you are asking the user to reconnect this link.",
    )
    institution_id: Optional[StrictStr] = Field(
        default=None,
        description="The ID of the institution you want to link to. Providing this will skip the institution         selection step. `existing_link_id` will take precedence over this field if both are provided.",
    )
    redirect_uri: Annotated[
        str, Field(min_length=1, strict=True, max_length=65536)
    ] = Field(
        description="For Oauth linking, a URI indicating the destination, in your application, where the user should         be sent after authenticating with the institution.  The `redirect_uri` should not contain any query parameters,         and it must be pre-approved by MoneyKit during the customer setup process."
    )
    webhook: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=65536)]
    ] = Field(
        default=None,
        description="The destination URL to which any webhooks should be sent.",
    )
    link_tags: Optional[List[StrictStr]] = None
    connect_features: Optional[MoneyKitConnectFeatures] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "settings",
        "customer_user",
        "existing_link_id",
        "institution_id",
        "redirect_uri",
        "webhook",
        "link_tags",
        "connect_features",
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
        """Create an instance of CreateLinkSessionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict["settings"] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_user
        if self.customer_user:
            _dict["customer_user"] = self.customer_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connect_features
        if self.connect_features:
            _dict["connect_features"] = self.connect_features.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateLinkSessionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "settings": LinkSessionSettingOverrides.from_dict(obj.get("settings"))
                if obj.get("settings") is not None
                else None,
                "customer_user": LinkSessionCustomerUser.from_dict(
                    obj.get("customer_user")
                )
                if obj.get("customer_user") is not None
                else None,
                "existing_link_id": obj.get("existing_link_id"),
                "institution_id": obj.get("institution_id"),
                "redirect_uri": obj.get("redirect_uri"),
                "webhook": obj.get("webhook"),
                "link_tags": obj.get("link_tags"),
                "connect_features": MoneyKitConnectFeatures.from_dict(
                    obj.get("connect_features")
                )
                if obj.get("connect_features") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
