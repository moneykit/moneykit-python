# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.account_import_data import AccountImportData


class TestAccountImportData(unittest.TestCase):
    """AccountImportData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountImportData:
        """Test AccountImportData
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AccountImportData`
        """
        model = AccountImportData()
        if include_optional:
            return AccountImportData(
                account_id = '74583934',
                name = 'Premier Checking',
                type = 'depository.checking',
                mask = '3748',
                balances = moneykit.models.account_balances.AccountBalances(
                    currency = 'USD', 
                    available = 340.12, 
                    current = 445.89, 
                    limit = 500, 
                    balance_date = '2021-08-12T15:23:00Z', )
            )
        else:
            return AccountImportData(
                account_id = '74583934',
                name = 'Premier Checking',
                type = 'depository.checking',
                balances = moneykit.models.account_balances.AccountBalances(
                    currency = 'USD', 
                    available = 340.12, 
                    current = 445.89, 
                    limit = 500, 
                    balance_date = '2021-08-12T15:23:00Z', ),
        )
        """

    def testAccountImportData(self):
        """Test AccountImportData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
