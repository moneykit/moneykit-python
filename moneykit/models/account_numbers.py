from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.ach_number import AchNumber
    from ..models.bacs_number import BacsNumber
    from ..models.eft_number import EftNumber
    from ..models.international_number import InternationalNumber


T = TypeVar("T", bound="AccountNumbers")


@attr.s(auto_attribs=True)
class AccountNumbers:
    """
    Attributes:
        ach (List['AchNumber']): List of ACH account numbers.
        bacs (List['BacsNumber']): List of BACS account numbers.
        eft (List['EftNumber']): List of EFT account numbers.
        international (List['InternationalNumber']): List of international account numbers.
    """

    ach: List["AchNumber"]
    bacs: List["BacsNumber"]
    eft: List["EftNumber"]
    international: List["InternationalNumber"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        ach = []
        for ach_item_data in self.ach:
            ach_item = ach_item_data.to_dict()

            ach.append(ach_item)

        bacs = []
        for bacs_item_data in self.bacs:
            bacs_item = bacs_item_data.to_dict()

            bacs.append(bacs_item)

        eft = []
        for eft_item_data in self.eft:
            eft_item = eft_item_data.to_dict()

            eft.append(eft_item)

        international = []
        for international_item_data in self.international:
            international_item = international_item_data.to_dict()

            international.append(international_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ach": ach,
                "bacs": bacs,
                "eft": eft,
                "international": international,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ach_number import AchNumber
        from ..models.bacs_number import BacsNumber
        from ..models.eft_number import EftNumber
        from ..models.international_number import InternationalNumber

        d = src_dict.copy()
        ach = []
        _ach = d.pop("ach")
        for ach_item_data in _ach:
            ach_item = AchNumber.from_dict(ach_item_data)

            ach.append(ach_item)

        bacs = []
        _bacs = d.pop("bacs")
        for bacs_item_data in _bacs:
            bacs_item = BacsNumber.from_dict(bacs_item_data)

            bacs.append(bacs_item)

        eft = []
        _eft = d.pop("eft")
        for eft_item_data in _eft:
            eft_item = EftNumber.from_dict(eft_item_data)

            eft.append(eft_item)

        international = []
        _international = d.pop("international")
        for international_item_data in _international:
            international_item = InternationalNumber.from_dict(international_item_data)

            international.append(international_item)

        account_numbers = cls(
            ach=ach,
            bacs=bacs,
            eft=eft,
            international=international,
        )

        account_numbers.additional_properties = d
        return account_numbers

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
