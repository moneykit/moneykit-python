from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.product import Product

T = TypeVar("T", bound="RefreshProductsRequest")


@attr.s(auto_attribs=True)
class RefreshProductsRequest:
    """
    Attributes:
        products (List[Product]): You can supply one or more products to refresh. If you do not supply any products, an
            error will be returned. Example: ['account_numbers', 'transactions'].
    """

    products: List[Product]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.value

            products.append(products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = Product(products_item_data)

            products.append(products_item)

        refresh_products_request = cls(
            products=products,
        )

        refresh_products_request.additional_properties = d
        return refresh_products_request

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
