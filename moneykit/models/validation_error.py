from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

T = TypeVar("T", bound="ValidationError")


@attr.s(auto_attribs=True)
class ValidationError:
    """
    Attributes:
        location (List[Union[int, str]]):
        message (str):
        type (str):
    """

    location: List[Union[int, str]]
    message: str
    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = []
        for location_item_data in self.location:
            location_item: Union[int, str]

            location_item = location_item_data

            location.append(location_item)

        message = self.message
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "message": message,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = []
        _location = d.pop("location")
        for location_item_data in _location:

            def _parse_location_item(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            location_item = _parse_location_item(location_item_data)

            location.append(location_item)

        message = d.pop("message")

        type = d.pop("type")

        validation_error = cls(
            location=location,
            message=message,
            type=type,
        )

        validation_error.additional_properties = d
        return validation_error

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
