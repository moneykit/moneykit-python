from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_user_transactions_response_accounts import GetUserTransactionsResponseAccounts
    from ..models.transaction import Transaction


T = TypeVar("T", bound="GetUserTransactionsResponse")


@attr.s(auto_attribs=True)
class GetUserTransactionsResponse:
    """
    Attributes:
        total (int): The total number of results for this query. Example: 82.
        page (int): The page number corresponding to this batch of results. Example: 1.
        size (int): The number of results in this batch. Example: 50.
        transactions (List['Transaction']):
        accounts (GetUserTransactionsResponseAccounts):
    """

    total: int
    page: int
    size: int
    transactions: List["Transaction"]
    accounts: "GetUserTransactionsResponseAccounts"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        page = self.page
        size = self.size
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()

            transactions.append(transactions_item)

        accounts = self.accounts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "page": page,
                "size": size,
                "transactions": transactions,
                "accounts": accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_user_transactions_response_accounts import GetUserTransactionsResponseAccounts
        from ..models.transaction import Transaction

        d = src_dict.copy()
        total = d.pop("total")

        page = d.pop("page")

        size = d.pop("size")

        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = Transaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        accounts = GetUserTransactionsResponseAccounts.from_dict(d.pop("accounts"))

        get_user_transactions_response = cls(
            total=total,
            page=page,
            size=size,
            transactions=transactions,
            accounts=accounts,
        )

        get_user_transactions_response.additional_properties = d
        return get_user_transactions_response

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
