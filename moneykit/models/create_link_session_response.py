from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateLinkSessionResponse")


@attr.s(auto_attribs=True)
class CreateLinkSessionResponse:
    """
    Attributes:
        link_session_token (str): A unique token identifying this link session. Example:
            c7318ff7-257c-490e-8242-03a815b223b7.
    """

    link_session_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_session_token = self.link_session_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link_session_token": link_session_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_session_token = d.pop("link_session_token")

        create_link_session_response = cls(
            link_session_token=link_session_token,
        )

        create_link_session_response.additional_properties = d
        return create_link_session_response

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
