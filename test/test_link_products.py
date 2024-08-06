# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.link_products import LinkProducts


class TestLinkProducts(unittest.TestCase):
    """LinkProducts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkProducts:
        """Test LinkProducts
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkProducts`
        """
        model = LinkProducts()
        if include_optional:
            return LinkProducts(
                accounts = moneykit.models.accounts_link_product.AccountsLinkProduct(
                    refreshed_at = '2023-02-16T09:14:11', 
                    last_attempted_at = '2023-02-16T09:14:11', ),
                account_numbers = moneykit.models.account_numbers_link_product.AccountNumbersLinkProduct(
                    refreshed_at = '2023-02-16T09:14:11', 
                    last_attempted_at = '2023-02-16T09:14:11', 
                    settings = moneykit.models.account_numbers_product_settings.AccountNumbersProductSettings(
                        required = True, 
                        prefetch = True, 
                        product = null, ), ),
                identity = moneykit.models.identity_link_product.IdentityLinkProduct(
                    refreshed_at = '2023-02-16T09:14:11', 
                    last_attempted_at = '2023-02-16T09:14:11', 
                    settings = moneykit.models.identity_product_settings.IdentityProductSettings(
                        required = True, 
                        prefetch = True, 
                        product = null, ), ),
                transactions = moneykit.models.transactions_link_product.TransactionsLinkProduct(
                    refreshed_at = '2023-02-16T09:14:11', 
                    last_attempted_at = '2023-02-16T09:14:11', 
                    settings = moneykit.models.transactions_product_settings.TransactionsProductSettings(
                        required = True, 
                        prefetch = True, 
                        product = null, 
                        extend_history = True, ), )
            )
        else:
            return LinkProducts(
        )
        """

    def testLinkProducts(self):
        """Test LinkProducts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
