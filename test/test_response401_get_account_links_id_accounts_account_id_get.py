# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.response401_get_account_links_id_accounts_account_id_get import (
    Response401GetAccountLinksIdAccountsAccountIdGet,
)


class TestResponse401GetAccountLinksIdAccountsAccountIdGet(unittest.TestCase):
    """Response401GetAccountLinksIdAccountsAccountIdGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> Response401GetAccountLinksIdAccountsAccountIdGet:
        """Test Response401GetAccountLinksIdAccountsAccountIdGet
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401GetAccountLinksIdAccountsAccountIdGet`
        """
        model = Response401GetAccountLinksIdAccountsAccountIdGet()
        if include_optional:
            return Response401GetAccountLinksIdAccountsAccountIdGet(
                error_code = link_error.unauthorized_access,
                error_message = None,
                documentation_url = None
            )
        else:
            return Response401GetAccountLinksIdAccountsAccountIdGet(
                error_message = None,
        )
        """

    def testResponse401GetAccountLinksIdAccountsAccountIdGet(self):
        """Test Response401GetAccountLinksIdAccountsAccountIdGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
