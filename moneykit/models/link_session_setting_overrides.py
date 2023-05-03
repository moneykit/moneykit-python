from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.country import Country
from ..models.provider import Provider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_permissions import LinkPermissions
    from ..models.products_settings import ProductsSettings


T = TypeVar("T", bound="LinkSessionSettingOverrides")


@attr.s(auto_attribs=True)
class LinkSessionSettingOverrides:
    """
    Attributes:
        providers (Union[Unset, None, List[Provider]]): If provided, restricts the available institutions to those
            supported
                        by **any** of these providers.
        link_permissions (Union[Unset, None, LinkPermissions]):
        products (Union[Unset, None, ProductsSettings]):
        countries (Union[Unset, None, List[Country]]): Restricts the available institutions to those in **any** of these
            countries.
    """

    providers: Union[Unset, None, List[Provider]] = UNSET
    link_permissions: Union[Unset, None, "LinkPermissions"] = UNSET
    products: Union[Unset, None, "ProductsSettings"] = UNSET
    countries: Union[Unset, None, List[Country]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        providers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.providers, Unset):
            if self.providers is None:
                providers = None
            else:
                providers = []
                for providers_item_data in self.providers:
                    providers_item = providers_item_data.value

                    providers.append(providers_item)

        link_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.link_permissions, Unset):
            link_permissions = self.link_permissions.to_dict() if self.link_permissions else None

        products: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict() if self.products else None

        countries: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            if self.countries is None:
                countries = None
            else:
                countries = []
                for countries_item_data in self.countries:
                    countries_item = countries_item_data.value

                    countries.append(countries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers
        if link_permissions is not UNSET:
            field_dict["link_permissions"] = link_permissions
        if products is not UNSET:
            field_dict["products"] = products
        if countries is not UNSET:
            field_dict["countries"] = countries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_permissions import LinkPermissions
        from ..models.products_settings import ProductsSettings

        d = src_dict.copy()
        providers = []
        _providers = d.pop("providers", UNSET)
        for providers_item_data in _providers or []:
            providers_item = Provider(providers_item_data)

            providers.append(providers_item)

        _link_permissions = d.pop("link_permissions", UNSET)
        link_permissions: Union[Unset, None, LinkPermissions]
        if _link_permissions is None:
            link_permissions = None
        elif isinstance(_link_permissions, Unset):
            link_permissions = UNSET
        else:
            link_permissions = LinkPermissions.from_dict(_link_permissions)

        _products = d.pop("products", UNSET)
        products: Union[Unset, None, ProductsSettings]
        if _products is None:
            products = None
        elif isinstance(_products, Unset):
            products = UNSET
        else:
            products = ProductsSettings.from_dict(_products)

        countries = []
        _countries = d.pop("countries", UNSET)
        for countries_item_data in _countries or []:
            countries_item = Country(countries_item_data)

            countries.append(countries_item)

        link_session_setting_overrides = cls(
            providers=providers,
            link_permissions=link_permissions,
            products=products,
            countries=countries,
        )

        link_session_setting_overrides.additional_properties = d
        return link_session_setting_overrides

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
