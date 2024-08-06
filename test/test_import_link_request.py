# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.import_link_request import ImportLinkRequest


class TestImportLinkRequest(unittest.TestCase):
    """ImportLinkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportLinkRequest:
        """Test ImportLinkRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ImportLinkRequest`
        """
        model = ImportLinkRequest()
        if include_optional:
            return ImportLinkRequest(
                customer_user = moneykit.models.customer_user.CustomerUser(
                    id = '0123', 
                    email = null, 
                    phone = null, ),
                provider = 'moneykit',
                institution_id = 'chase',
                accounts = [
                    moneykit.models.account_import_data.AccountImportData(
                        account_id = '74583934', 
                        name = 'Premier Checking', 
                        type = 'depository.checking', 
                        mask = '3748', 
                        balances = null, )
                    ],
                transactions = [
                    moneykit.models.transaction_import_data.TransactionImportData(
                        account_id = '74583934', 
                        transaction_id = '', 
                        amount = '384.05', 
                        date = null, 
                        description = 'Regina's Mulberry', 
                        type = 'food_and_drinks.restaurants', )
                    ]
            )
        else:
            return ImportLinkRequest(
                customer_user = moneykit.models.customer_user.CustomerUser(
                    id = '0123', 
                    email = null, 
                    phone = null, ),
                institution_id = 'chase',
                accounts = [
                    moneykit.models.account_import_data.AccountImportData(
                        account_id = '74583934', 
                        name = 'Premier Checking', 
                        type = 'depository.checking', 
                        mask = '3748', 
                        balances = null, )
                    ],
                transactions = [
                    moneykit.models.transaction_import_data.TransactionImportData(
                        account_id = '74583934', 
                        transaction_id = '', 
                        amount = '384.05', 
                        date = null, 
                        description = 'Regina's Mulberry', 
                        type = 'food_and_drinks.restaurants', )
                    ],
        )
        """

    def testImportLinkRequest(self):
        """Test ImportLinkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
