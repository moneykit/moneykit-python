from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.currency import Currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountBalances")


@attr.s(auto_attribs=True)
class AccountBalances:
    """
    Attributes:
        currency (Currency): ISO 4217 currency.  Its enumerants are ISO 4217 currencies except for
            some special currencies like ```XXX``.  Enumerants names are lowercase
            cureency code e.g. :attr:`Currency.eur`, :attr:`Currency.usd`.
        available (Union[Unset, None, float]): The amount of funds available for use.  Not all institutions report the
            available balance.
                        <p>Note that the available balance typically does not include overdraft limits. Example: 340.12.
        current (Union[Unset, None, float]): The total amount of funds in the account.
                        <p>For credit or loan accounts, a positive number indicates the amount owed by the account holder.
                        If the balance is negative (this is rare), this indicates an amount owed **to** the account holder.
                        <p>For depository or investment accounts, a positive number is the asset value of the account.
                        If the balance is negative (this is rare), this indicates an overdraft or margin condition. Example:
            445.89.
        limit (Union[Unset, None, float]): The credit limit on the account.  Typically this exists only for credit-type
            accounts.
                        <p>In some cases, this may represent the overdraft limit for depository accounts. Example: 500.
    """

    currency: Currency
    available: Union[Unset, None, float] = UNSET
    current: Union[Unset, None, float] = UNSET
    limit: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency.value

        available = self.available
        current = self.current
        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
            }
        )
        if available is not UNSET:
            field_dict["available"] = available
        if current is not UNSET:
            field_dict["current"] = current
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = Currency(d.pop("currency"))

        available = d.pop("available", UNSET)

        current = d.pop("current", UNSET)

        limit = d.pop("limit", UNSET)

        account_balances = cls(
            currency=currency,
            available=available,
            current=current,
            limit=limit,
        )

        account_balances.additional_properties = d
        return account_balances

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
