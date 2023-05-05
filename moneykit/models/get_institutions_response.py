from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.institution import Institution


T = TypeVar("T", bound="GetInstitutionsResponse")


@attr.s(auto_attribs=True)
class GetInstitutionsResponse:
    """
    Attributes:
        institutions (List['Institution']): The list of institutions for this page.
        cursors (CursorPagination):
    """

    institutions: List["Institution"]
    cursors: "CursorPagination"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        institutions = []
        for institutions_item_data in self.institutions:
            institutions_item = institutions_item_data.to_dict()

            institutions.append(institutions_item)

        cursors = self.cursors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutions": institutions,
                "cursors": cursors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.institution import Institution

        d = src_dict.copy()
        institutions = []
        _institutions = d.pop("institutions")
        for institutions_item_data in _institutions:
            institutions_item = Institution.from_dict(institutions_item_data)

            institutions.append(institutions_item)

        cursors = CursorPagination.from_dict(d.pop("cursors"))

        get_institutions_response = cls(
            institutions=institutions,
            cursors=cursors,
        )

        get_institutions_response.additional_properties = d
        return get_institutions_response

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
