from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_numbers_link_product import AccountNumbersLinkProduct
    from ..models.accounts_link_product import AccountsLinkProduct
    from ..models.identity_link_product import IdentityLinkProduct
    from ..models.transactions_link_product import TransactionsLinkProduct


T = TypeVar("T", bound="LinkProducts")


@attr.s(auto_attribs=True)
class LinkProducts:
    """
    Attributes:
        accounts (Union[Unset, AccountsLinkProduct]):
        account_numbers (Union[Unset, AccountNumbersLinkProduct]):
        identity (Union[Unset, IdentityLinkProduct]):
        transactions (Union[Unset, TransactionsLinkProduct]):
    """

    accounts: Union[Unset, "AccountsLinkProduct"] = UNSET
    account_numbers: Union[Unset, "AccountNumbersLinkProduct"] = UNSET
    identity: Union[Unset, "IdentityLinkProduct"] = UNSET
    transactions: Union[Unset, "TransactionsLinkProduct"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        accounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts.to_dict()

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
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if account_numbers is not UNSET:
            field_dict["account_numbers"] = account_numbers
        if identity is not UNSET:
            field_dict["identity"] = identity
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_numbers_link_product import AccountNumbersLinkProduct
        from ..models.accounts_link_product import AccountsLinkProduct
        from ..models.identity_link_product import IdentityLinkProduct
        from ..models.transactions_link_product import TransactionsLinkProduct

        d = src_dict.copy()
        _accounts = d.pop("accounts", UNSET)
        accounts: Union[Unset, AccountsLinkProduct]
        if isinstance(_accounts, Unset):
            accounts = UNSET
        else:
            accounts = AccountsLinkProduct.from_dict(_accounts)

        _account_numbers = d.pop("account_numbers", UNSET)
        account_numbers: Union[Unset, AccountNumbersLinkProduct]
        if isinstance(_account_numbers, Unset):
            account_numbers = UNSET
        else:
            account_numbers = AccountNumbersLinkProduct.from_dict(_account_numbers)

        _identity = d.pop("identity", UNSET)
        identity: Union[Unset, IdentityLinkProduct]
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = IdentityLinkProduct.from_dict(_identity)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, TransactionsLinkProduct]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = TransactionsLinkProduct.from_dict(_transactions)

        link_products = cls(
            accounts=accounts,
            account_numbers=account_numbers,
            identity=identity,
            transactions=transactions,
        )

        link_products.additional_properties = d
        return link_products

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
