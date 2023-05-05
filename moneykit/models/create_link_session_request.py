from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_session_customer_user import LinkSessionCustomerUser
    from ..models.link_session_setting_overrides import LinkSessionSettingOverrides
    from ..models.money_link_features import MoneyLinkFeatures


T = TypeVar("T", bound="CreateLinkSessionRequest")


@attr.s(auto_attribs=True)
class CreateLinkSessionRequest:
    """
    Attributes:
        customer_user (LinkSessionCustomerUser):
        settings (Union[Unset, None, LinkSessionSettingOverrides]):
        existing_link_id (Union[Unset, None, str]): Supply the existing `link_id` if you are asking the user to
            reconnect this link. Example: c7318ff7-257c-490e-8242-03a815b223b7.
        redirect_uri (Union[Unset, None, str]): For Oauth linking, a URI indicating the destination, in your
            application, where the user should
                    be sent after authenticating with the institution.  The `redirect_uri` should not contain any query
            parameters,
                    and it must be pre-approved by MoneyKit during the customer setup process. Example:
            https://yourdomain.com/oauth.html.
        webhook (Union[Unset, None, str]): The destination URL to which any webhooks should be sent. Example:
            https://yourdomain.com/moneykit_webhook.
        link_tags (Union[Unset, List[str]]): You can supply one or more arbitrary strings as tags to describe this link.
            Example: ['smoke_test', 'user_type:admin'].
        moneylink_features (Union[Unset, MoneyLinkFeatures]):
    """

    customer_user: "LinkSessionCustomerUser"
    settings: Union[Unset, None, "LinkSessionSettingOverrides"] = UNSET
    existing_link_id: Union[Unset, None, str] = UNSET
    redirect_uri: Union[Unset, None, str] = UNSET
    webhook: Union[Unset, None, str] = UNSET
    link_tags: Union[Unset, List[str]] = UNSET
    moneylink_features: Union[Unset, "MoneyLinkFeatures"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_user = self.customer_user.to_dict()

        settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict() if self.settings else None

        existing_link_id = self.existing_link_id
        redirect_uri = self.redirect_uri
        webhook = self.webhook
        link_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.link_tags, Unset):
            link_tags = self.link_tags

        moneylink_features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.moneylink_features, Unset):
            moneylink_features = self.moneylink_features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_user": customer_user,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings
        if existing_link_id is not UNSET:
            field_dict["existing_link_id"] = existing_link_id
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if link_tags is not UNSET:
            field_dict["link_tags"] = link_tags
        if moneylink_features is not UNSET:
            field_dict["moneylink_features"] = moneylink_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_session_customer_user import LinkSessionCustomerUser
        from ..models.link_session_setting_overrides import LinkSessionSettingOverrides
        from ..models.money_link_features import MoneyLinkFeatures

        d = src_dict.copy()
        customer_user = LinkSessionCustomerUser.from_dict(d.pop("customer_user"))

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, None, LinkSessionSettingOverrides]
        if _settings is None:
            settings = None
        elif isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = LinkSessionSettingOverrides.from_dict(_settings)

        existing_link_id = d.pop("existing_link_id", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        webhook = d.pop("webhook", UNSET)

        link_tags = cast(List[str], d.pop("link_tags", UNSET))

        _moneylink_features = d.pop("moneylink_features", UNSET)
        moneylink_features: Union[Unset, MoneyLinkFeatures]
        if isinstance(_moneylink_features, Unset):
            moneylink_features = UNSET
        else:
            moneylink_features = MoneyLinkFeatures.from_dict(_moneylink_features)

        create_link_session_request = cls(
            customer_user=customer_user,
            settings=settings,
            existing_link_id=existing_link_id,
            redirect_uri=redirect_uri,
            webhook=webhook,
            link_tags=link_tags,
            moneylink_features=moneylink_features,
        )

        create_link_session_request.additional_properties = d
        return create_link_session_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
