# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.customer_user import CustomerUser


class TestCustomerUser(unittest.TestCase):
    """CustomerUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerUser:
        """Test CustomerUser
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CustomerUser`
        """
        model = CustomerUser()
        if include_optional:
            return CustomerUser(
                id = '0123',
                email = moneykit.models.customer_user_email.CustomerUserEmail(
                    address = '0123', 
                    customer_verified_at = '2023-02-16T00:00:00', ),
                phone = moneykit.models.customer_user_phone.CustomerUserPhone(
                    number = '+16175551212', 
                    country = null, 
                    customer_verified_at = '2023-02-16T00:00:00', )
            )
        else:
            return CustomerUser(
                id = '0123',
        )
        """

    def testCustomerUser(self):
        """Test CustomerUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
