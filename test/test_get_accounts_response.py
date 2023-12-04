# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.get_accounts_response import GetAccountsResponse


class TestGetAccountsResponse(unittest.TestCase):
    """GetAccountsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountsResponse:
        """Test GetAccountsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetAccountsResponse`
        """
        model = GetAccountsResponse()
        if include_optional:
            return GetAccountsResponse(
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
            return GetAccountsResponse(
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

    def testGetAccountsResponse(self):
        """Test GetAccountsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()