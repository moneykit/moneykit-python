# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.api_public_users_transactions_legacy_get_user_transactions_response import (
    ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse,
)


class TestApiPublicUsersTransactionsLegacyGetUserTransactionsResponse(
    unittest.TestCase
):
    """ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse:
        """Test ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse`
        """
        model = ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse()
        if include_optional:
            return ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse(
                total = 82,
                page = 1,
                size = 50,
                transactions = [
                    moneykit.models.transaction.Transaction(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = 'food_and_drinks.restaurants', )
                    ],
                accounts = {
                    'key' : moneykit.models.basic_account_details.BasicAccountDetails(
                        name = 'Premier Checking', 
                        last_synced_at = '2023-02-16T09:14:11', 
                        institution_id = '', 
                        link_id = '', )
                    }
            )
        else:
            return ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse(
                total = 82,
                page = 1,
                size = 50,
                transactions = [
                    moneykit.models.transaction.Transaction(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = 'food_and_drinks.restaurants', )
                    ],
                accounts = {
                    'key' : moneykit.models.basic_account_details.BasicAccountDetails(
                        name = 'Premier Checking', 
                        last_synced_at = '2023-02-16T09:14:11', 
                        institution_id = '', 
                        link_id = '', )
                    },
        )
        """

    def testApiPublicUsersTransactionsLegacyGetUserTransactionsResponse(self):
        """Test ApiPublicUsersTransactionsLegacyGetUserTransactionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
