# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.account_numbers_product_settings import (
    AccountNumbersProductSettings,
)


class TestAccountNumbersProductSettings(unittest.TestCase):
    """AccountNumbersProductSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountNumbersProductSettings:
        """Test AccountNumbersProductSettings
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AccountNumbersProductSettings`
        """
        model = AccountNumbersProductSettings()
        if include_optional:
            return AccountNumbersProductSettings(
                required = True,
                prefetch = True,
                product = 'accounts'
            )
        else:
            return AccountNumbersProductSettings(
        )
        """

    def testAccountNumbersProductSettings(self):
        """Test AccountNumbersProductSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
