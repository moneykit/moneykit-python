from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InternationalNumber")


@attr.s(auto_attribs=True)
class InternationalNumber:
    """
    Attributes:
        iban (str): The IBAN.
        bic (str): The BIC.
    """

    iban: str
    bic: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iban = self.iban
        bic = self.bic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iban": iban,
                "bic": bic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iban = d.pop("iban")

        bic = d.pop("bic")

        international_number = cls(
            iban=iban,
            bic=bic,
        )

        international_number.additional_properties = d
        return international_number

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
