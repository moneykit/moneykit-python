from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_session_customer_user_email import LinkSessionCustomerUserEmail
    from ..models.link_session_customer_user_phone import LinkSessionCustomerUserPhone


T = TypeVar("T", bound="LinkSessionCustomerUser")


@attr.s(auto_attribs=True)
class LinkSessionCustomerUser:
    """
    Attributes:
        id (str): Your own unique ID for this user.  Typically this will be a UUID or primary key
                    from your application.
        email (Union[Unset, None, LinkSessionCustomerUserEmail]):
        phone (Union[Unset, None, LinkSessionCustomerUserPhone]):
    """

    id: str
    email: Union[Unset, None, "LinkSessionCustomerUserEmail"] = UNSET
    phone: Union[Unset, None, "LinkSessionCustomerUserPhone"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict() if self.email else None

        phone: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.to_dict() if self.phone else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_session_customer_user_email import LinkSessionCustomerUserEmail
        from ..models.link_session_customer_user_phone import LinkSessionCustomerUserPhone

        d = src_dict.copy()
        id = d.pop("id")

        _email = d.pop("email", UNSET)
        email: Union[Unset, None, LinkSessionCustomerUserEmail]
        if _email is None:
            email = None
        elif isinstance(_email, Unset):
            email = UNSET
        else:
            email = LinkSessionCustomerUserEmail.from_dict(_email)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, None, LinkSessionCustomerUserPhone]
        if _phone is None:
            phone = None
        elif isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = LinkSessionCustomerUserPhone.from_dict(_phone)

        link_session_customer_user = cls(
            id=id,
            email=email,
            phone=phone,
        )

        link_session_customer_user.additional_properties = d
        return link_session_customer_user

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
