import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.transaction_type import TransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@attr.s(auto_attribs=True)
class Transaction:
    """
    Attributes:
        transaction_id (str): The unique ID for this transaction. Example: c7318ff7-257c-490e-8242-03a815b223b7.
        account_id (str): The ID of the account in which this transaction occurred. Example:
            a3ba443a-257c-490e-8242-03a84789d39f.
        amount (str): The amount of this transaction, denominated in account currency.  This amount is always
                    non-negative.  The `type` field indicates whether it is entering or leaving the account. Example:
            384.05.
        type (TransactionType): An enumeration.
        currency (str): The ISO-4217 currency code of the transaction. Example: USD.
        date (datetime.date): The effective (posted) date the transaction, in ISO-8601 format.  For pending
            transactions,
                        this date is when the transaction was initiated. Example: 2023-02-16T00:00:00.
        pending (bool): If true, this transaction is pending or unsettled and has not yet affected the account.
                    Commonly these are credit card transactions, particularly approvals (holds) such as for hotel or
            restaurant
                    reservations placed in advance where the final amount is still to be determined.
        description (Union[Unset, None, str]): A normalized, cleaned transaction description suitable for presentation
            to the end user.
                        Commonly this will be the merchant or counterparty name. Example: Regina's Mulberry.
        raw_description (Union[Unset, None, str]): The raw transaction description as provided by the institution, where
            available. Example: Regina's Mulberry #1402 T48999-84.
        category (Union[Unset, None, str]): The category for this transaction, given as a dotted string indicating a
            hierarchical
                    categorization.  See <a href=/pages/categories>Transaction Categories</a> for the list of possible
            transaction types. Example: food_and_drinks.restaurants.
    """

    transaction_id: str
    account_id: str
    amount: str
    type: TransactionType
    currency: str
    date: datetime.date
    pending: bool
    description: Union[Unset, None, str] = UNSET
    raw_description: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id
        account_id = self.account_id
        amount = self.amount
        type = self.type.value

        currency = self.currency
        date = self.date.isoformat()
        pending = self.pending
        description = self.description
        raw_description = self.raw_description
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction_id": transaction_id,
                "account_id": account_id,
                "amount": amount,
                "type": type,
                "currency": currency,
                "date": date,
                "pending": pending,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if raw_description is not UNSET:
            field_dict["raw_description"] = raw_description
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transaction_id")

        account_id = d.pop("account_id")

        amount = d.pop("amount")

        type = TransactionType(d.pop("type"))

        currency = d.pop("currency")

        date = isoparse(d.pop("date")).date()

        pending = d.pop("pending")

        description = d.pop("description", UNSET)

        raw_description = d.pop("raw_description", UNSET)

        category = d.pop("category", UNSET)

        transaction = cls(
            transaction_id=transaction_id,
            account_id=account_id,
            amount=amount,
            type=type,
            currency=currency,
            date=date,
            pending=pending,
            description=description,
            raw_description=raw_description,
            category=category,
        )

        transaction.additional_properties = d
        return transaction

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
