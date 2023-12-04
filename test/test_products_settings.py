# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.products_settings import ProductsSettings


class TestProductsSettings(unittest.TestCase):
    """ProductsSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductsSettings:
        """Test ProductsSettings
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProductsSettings`
        """
        model = ProductsSettings()
        if include_optional:
            return ProductsSettings(
                account_numbers = moneykit.models.account_numbers_product_settings.AccountNumbersProductSettings(
                    required = True, 
                    prefetch = True, 
                    product = null, ),
                identity = moneykit.models.identity_product_settings.IdentityProductSettings(
                    required = True, 
                    prefetch = True, 
                    product = null, ),
                transactions = moneykit.models.transactions_product_settings.TransactionsProductSettings(
                    required = True, 
                    prefetch = True, 
                    product = null, 
                    extend_history = True, ),
                investments = moneykit.models.investments_product_settings.InvestmentsProductSettings(
                    required = True, 
                    prefetch = True, 
                    product = null, )
            )
        else:
            return ProductsSettings(
        )
        """

    def testProductsSettings(self):
        """Test ProductsSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
