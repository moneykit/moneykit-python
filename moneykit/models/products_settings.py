from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_numbers_product_settings import AccountNumbersProductSettings
    from ..models.identity_product_settings import IdentityProductSettings
    from ..models.transactions_product_settings import TransactionsProductSettings


T = TypeVar("T", bound="ProductsSettings")


@attr.s(auto_attribs=True)
class ProductsSettings:
    """
    Attributes:
        account_numbers (Union[Unset, AccountNumbersProductSettings]):
        identity (Union[Unset, IdentityProductSettings]):
        transactions (Union[Unset, TransactionsProductSettings]):
    """

    account_numbers: Union[Unset, "AccountNumbersProductSettings"] = UNSET
    identity: Union[Unset, "IdentityProductSettings"] = UNSET
    transactions: Union[Unset, "TransactionsProductSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        account_numbers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_numbers, Unset):
            account_numbers = self.account_numbers.to_dict()

        identity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = self.transactions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_numbers is not UNSET:
            field_dict["account_numbers"] = account_numbers
        if identity is not UNSET:
            field_dict["identity"] = identity
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_numbers_product_settings import AccountNumbersProductSettings
        from ..models.identity_product_settings import IdentityProductSettings
        from ..models.transactions_product_settings import TransactionsProductSettings

        d = src_dict.copy()
        _account_numbers = d.pop("account_numbers", UNSET)
        account_numbers: Union[Unset, AccountNumbersProductSettings]
        if isinstance(_account_numbers, Unset):
            account_numbers = UNSET
        else:
            account_numbers = AccountNumbersProductSettings.from_dict(_account_numbers)

        _identity = d.pop("identity", UNSET)
        identity: Union[Unset, IdentityProductSettings]
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = IdentityProductSettings.from_dict(_identity)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, TransactionsProductSettings]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = TransactionsProductSettings.from_dict(_transactions)

        products_settings = cls(
            account_numbers=account_numbers,
            identity=identity,
            transactions=transactions,
        )

        products_settings.additional_properties = d
        return products_settings

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
