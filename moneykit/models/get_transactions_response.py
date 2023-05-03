from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.link_common import LinkCommon
    from ..models.transaction import Transaction


T = TypeVar("T", bound="GetTransactionsResponse")


@attr.s(auto_attribs=True)
class GetTransactionsResponse:
    """
    Attributes:
        total (int): The total number of results for this query. Example: 82.
        page (int): The page number corresponding to this batch of results. Example: 1.
        size (int): The number of results in this batch. Example: 50.
        transactions (List['Transaction']): A list of transactions.
        accounts (List['Account']): A list of accounts for which transactions are being returned.
        link (LinkCommon):  Example: {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase',
            'institution_name': 'Chase', 'provider': 'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11',
            'tags': ['user_type:admin'], 'products': {'accounts': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11'}, 'identity': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required': True, 'prefetch': False}}}}.
    """

    total: int
    page: int
    size: int
    transactions: List["Transaction"]
    accounts: List["Account"]
    link: "LinkCommon"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        total = self.total
        page = self.page
        size = self.size
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()

            transactions.append(transactions_item)

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()

            accounts.append(accounts_item)

        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "page": page,
                "size": size,
                "transactions": transactions,
                "accounts": accounts,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.link_common import LinkCommon
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

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        link = LinkCommon.from_dict(d.pop("link"))

        get_transactions_response = cls(
            total=total,
            page=page,
            size=size,
            transactions=transactions,
            accounts=accounts,
            link=link,
        )

        get_transactions_response.additional_properties = d
        return get_transactions_response

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
