# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.response401_get_transactions_diff_links_id_transactions_sync_get import (
    Response401GetTransactionsDiffLinksIdTransactionsSyncGet,
)


class TestResponse401GetTransactionsDiffLinksIdTransactionsSyncGet(unittest.TestCase):
    """Response401GetTransactionsDiffLinksIdTransactionsSyncGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> Response401GetTransactionsDiffLinksIdTransactionsSyncGet:
        """Test Response401GetTransactionsDiffLinksIdTransactionsSyncGet
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401GetTransactionsDiffLinksIdTransactionsSyncGet`
        """
        model = Response401GetTransactionsDiffLinksIdTransactionsSyncGet()
        if include_optional:
            return Response401GetTransactionsDiffLinksIdTransactionsSyncGet(
                error_code = link_error.unauthorized_access,
                error_message = None,
                documentation_url = None
            )
        else:
            return Response401GetTransactionsDiffLinksIdTransactionsSyncGet(
                error_message = None,
        )
        """

    def testResponse401GetTransactionsDiffLinksIdTransactionsSyncGet(self):
        """Test Response401GetTransactionsDiffLinksIdTransactionsSyncGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()