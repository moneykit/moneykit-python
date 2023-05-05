from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account_type import AccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balances import AccountBalances
    from ..models.account_numbers import AccountNumbers


T = TypeVar("T", bound="AccountWithAccountNumbers")


@attr.s(auto_attribs=True)
class AccountWithAccountNumbers:
    """
    Attributes:
        account_id (str): MoneyKit's unique ID for the account.
                    <p>The `account_id` is distinct from the institution's account number.  For accounts that may change
            account
                    numbers from time to time, such as credit cards, MoneyKit attempts to keep the `account_id` constant.
                    However, if MoneyKit can't reconcile the new account data with the old data, the `account_id` may
            change. Example: c7318ff7-257c-490e-8242-03a815b223b7.
        account_type (AccountType): An enumeration.
        name (str): The account name, according to the institution.  Note that some institutions allow
                    the end user to nickname the account; in such cases this field may be the name assigned by the user
            Example: Premier Checking.
        balances (AccountBalances):
        numbers (AccountNumbers):
        account_mask (Union[Unset, None, str]): The last four characters (usually digits) of the account number.
                    Note that this mask may be non-unique between accounts. Example: 3748.
    """

    account_id: str
    account_type: AccountType
    name: str
    balances: "AccountBalances"
    numbers: "AccountNumbers"
    account_mask: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        account_type = self.account_type.value

        name = self.name
        balances = self.balances.to_dict()

        numbers = self.numbers.to_dict()

        account_mask = self.account_mask

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "account_type": account_type,
                "name": name,
                "balances": balances,
                "numbers": numbers,
            }
        )
        if account_mask is not UNSET:
            field_dict["account_mask"] = account_mask

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_balances import AccountBalances
        from ..models.account_numbers import AccountNumbers

        d = src_dict.copy()
        account_id = d.pop("account_id")

        account_type = AccountType(d.pop("account_type"))

        name = d.pop("name")

        balances = AccountBalances.from_dict(d.pop("balances"))

        numbers = AccountNumbers.from_dict(d.pop("numbers"))

        account_mask = d.pop("account_mask", UNSET)

        account_with_account_numbers = cls(
            account_id=account_id,
            account_type=account_type,
            name=name,
            balances=balances,
            numbers=numbers,
            account_mask=account_mask,
        )

        account_with_account_numbers.additional_properties = d
        return account_with_account_numbers

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
