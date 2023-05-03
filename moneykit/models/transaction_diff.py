from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

if TYPE_CHECKING:
    from ..models.transaction import Transaction


T = TypeVar("T", bound="TransactionDiff")


@attr.s(auto_attribs=True)
class TransactionDiff:
    """
    Attributes:
        created (List['Transaction']): A list of transactions that have been added to the link ordered by ascending
            datetime.
        updated (List['Transaction']): A list of transactions that have been updated on the link ordered by ascending
            datetime.
        removed (List[str]): A list of transaction ids that have been removed from the link ordered by ascending
            datetime.
    """

    created: List["Transaction"]
    updated: List["Transaction"]
    removed: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        created = []
        for created_item_data in self.created:
            created_item = created_item_data.to_dict()

            created.append(created_item)

        updated = []
        for updated_item_data in self.updated:
            updated_item = updated_item_data.to_dict()

            updated.append(updated_item)

        removed = self.removed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction import Transaction

        d = src_dict.copy()
        created = []
        _created = d.pop("created")
        for created_item_data in _created:
            created_item = Transaction.from_dict(created_item_data)

            created.append(created_item)

        updated = []
        _updated = d.pop("updated")
        for updated_item_data in _updated:
            updated_item = Transaction.from_dict(updated_item_data)

            updated.append(updated_item)

        removed = cast(List[str], d.pop("removed"))

        transaction_diff = cls(
            created=created,
            updated=updated,
            removed=removed,
        )

        transaction_diff.additional_properties = d
        return transaction_diff

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
