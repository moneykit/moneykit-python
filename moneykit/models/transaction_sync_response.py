from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.link_common import LinkCommon
    from ..models.transaction_diff import TransactionDiff


T = TypeVar("T", bound="TransactionSyncResponse")


@attr.s(auto_attribs=True)
class TransactionSyncResponse:
    """
    Attributes:
        transactions (TransactionDiff):
        cursor (CursorPagination):
        has_more (bool): This condition indicates the presence of transaction updates exceeding the requested count.
                    If true, additional updates can be retrieved by making an additional request with cursor set to
            next_cursor.
        link (LinkCommon):  Example: {'link_id': 'mk_eqkWN34UEoa2NxyALG8pcV', 'institution_id': 'chase',
            'institution_name': 'Chase', 'provider': 'mx', 'state': 'connected', 'last_synced_at': '2023-02-16T09:14:11',
            'tags': ['user_type:admin'], 'products': {'accounts': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11'}, 'identity': {'refreshed_at': '2023-02-16T09:14:11',
            'last_attempted_at': '2023-02-16T09:14:11', 'settings': {'required': True, 'prefetch': False}}}}.
    """

    transactions: "TransactionDiff"
    cursor: "CursorPagination"
    has_more: bool
    link: "LinkCommon"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        transactions = self.transactions.to_dict()

        cursor = self.cursor.to_dict()

        has_more = self.has_more
        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
                "cursor": cursor,
                "has_more": has_more,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.link_common import LinkCommon
        from ..models.transaction_diff import TransactionDiff

        d = src_dict.copy()
        transactions = TransactionDiff.from_dict(d.pop("transactions"))

        cursor = CursorPagination.from_dict(d.pop("cursor"))

        has_more = d.pop("has_more")

        link = LinkCommon.from_dict(d.pop("link"))

        transaction_sync_response = cls(
            transactions=transactions,
            cursor=cursor,
            has_more=has_more,
            link=link,
        )

        transaction_sync_response.additional_properties = d
        return transaction_sync_response

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
