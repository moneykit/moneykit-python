# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.account_with_account_numbers_legacy20230218 import (
    AccountWithAccountNumbersLegacy20230218,
)


class TestAccountWithAccountNumbersLegacy20230218(unittest.TestCase):
    """AccountWithAccountNumbersLegacy20230218 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AccountWithAccountNumbersLegacy20230218:
        """Test AccountWithAccountNumbersLegacy20230218
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AccountWithAccountNumbersLegacy20230218`
        """
        model = AccountWithAccountNumbersLegacy20230218()
        if include_optional:
            return AccountWithAccountNumbersLegacy20230218(
                account_id = 'acc_6Tef269B6ZArSVpYrxtjBV',
                account_type = 'depository.checking',
                name = 'Premier Checking',
                account_mask = '3748',
                balances = moneykit.models.account_balances.AccountBalances(
                    currency = USD, 
                    available = 340.12, 
                    current = 445.89, 
                    limit = 500, 
                    balance_date = '2021-08-12T15:23:00Z', ),
                numbers = moneykit.models.account_numbers_legacy_2023_02_18.AccountNumbersLegacy_2023_02_18(
                    ach = [
                        moneykit.models.ach_number.AchNumber(
                            account_number = '', 
                            routing_number = '', 
                            wire_routing_number = '', )
                        ], 
                    bacs = [
                        moneykit.models.bacs_number.BacsNumber(
                            account_number = '', 
                            sort_code = '', )
                        ], 
                    eft = [
                        moneykit.models.eft_number.EftNumber(
                            account_number = '', 
                            institution_number = '', 
                            branch_number = '', )
                        ], 
                    international = [
                        moneykit.models.international_number.InternationalNumber(
                            iban = '', 
                            bic = '', )
                        ], )
            )
        else:
            return AccountWithAccountNumbersLegacy20230218(
                account_id = 'acc_6Tef269B6ZArSVpYrxtjBV',
                account_type = 'depository.checking',
                name = 'Premier Checking',
                balances = moneykit.models.account_balances.AccountBalances(
                    currency = USD, 
                    available = 340.12, 
                    current = 445.89, 
                    limit = 500, 
                    balance_date = '2021-08-12T15:23:00Z', ),
                numbers = moneykit.models.account_numbers_legacy_2023_02_18.AccountNumbersLegacy_2023_02_18(
                    ach = [
                        moneykit.models.ach_number.AchNumber(
                            account_number = '', 
                            routing_number = '', 
                            wire_routing_number = '', )
                        ], 
                    bacs = [
                        moneykit.models.bacs_number.BacsNumber(
                            account_number = '', 
                            sort_code = '', )
                        ], 
                    eft = [
                        moneykit.models.eft_number.EftNumber(
                            account_number = '', 
                            institution_number = '', 
                            branch_number = '', )
                        ], 
                    international = [
                        moneykit.models.international_number.InternationalNumber(
                            iban = '', 
                            bic = '', )
                        ], ),
        )
        """

    def testAccountWithAccountNumbersLegacy20230218(self):
        """Test AccountWithAccountNumbersLegacy20230218"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
