# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.get_transactions_response import GetTransactionsResponse


class TestGetTransactionsResponse(unittest.TestCase):
    """GetTransactionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTransactionsResponse:
        """Test GetTransactionsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetTransactionsResponse`
        """
        model = GetTransactionsResponse()
        if include_optional:
            return GetTransactionsResponse(
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
                accounts = [
                    moneykit.models.account.Account(
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        account_type = 'depository.checking', 
                        name = 'Premier Checking', 
                        account_mask = '3748', 
                        balances = null, )
                    ],
                link = {link_id=mk_eqkWN34UEoa2NxyALG8pcV, institution_id=chase, institution_name=Chase, provider=mx, state=connected, last_synced_at=2023-02-16T09:14:11, tags=[user_type:admin], products={accounts={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11}, identity={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11, settings={required=true, prefetch=false}}}}
            )
        else:
            return GetTransactionsResponse(
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
                accounts = [
                    moneykit.models.account.Account(
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        account_type = 'depository.checking', 
                        name = 'Premier Checking', 
                        account_mask = '3748', 
                        balances = null, )
                    ],
                link = {link_id=mk_eqkWN34UEoa2NxyALG8pcV, institution_id=chase, institution_name=Chase, provider=mx, state=connected, last_synced_at=2023-02-16T09:14:11, tags=[user_type:admin], products={accounts={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11}, identity={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11, settings={required=true, prefetch=false}}}},
        )
        """

    def testGetTransactionsResponse(self):
        """Test GetTransactionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()