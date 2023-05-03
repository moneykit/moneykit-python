from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CustomerApp")


@attr.s(auto_attribs=True)
class CustomerApp:
    """Customer Application for a specific environment

    Attributes:
        id (str): Your app's ID. Example: 3d18cdd1-fa96-4423-b781-bd5be036830e.
        app_name (str): Your app's name. Example: My App.
    """

    id: str
    app_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        app_name = self.app_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app_name": app_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        app_name = d.pop("app_name")

        customer_app = cls(
            id=id,
            app_name=app_name,
        )

        customer_app.additional_properties = d
        return customer_app

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
