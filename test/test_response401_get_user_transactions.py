# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.response401_get_user_transactions import (
    Response401GetUserTransactions,
)


class TestResponse401GetUserTransactions(unittest.TestCase):
    """Response401GetUserTransactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Response401GetUserTransactions:
        """Test Response401GetUserTransactions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401GetUserTransactions`
        """
        model = Response401GetUserTransactions()
        if include_optional:
            return Response401GetUserTransactions(
                error_code = api_error.auth.unauthorized,
                error_message = Accounts access not permitted,
                documentation_url = None
            )
        else:
            return Response401GetUserTransactions(
                error_message = Accounts access not permitted,
        )
        """

    def testResponse401GetUserTransactions(self):
        """Test Response401GetUserTransactions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
