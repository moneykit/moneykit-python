# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.link_product import LinkProduct


class TestLinkProduct(unittest.TestCase):
    """LinkProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkProduct:
        """Test LinkProduct
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkProduct`
        """
        model = LinkProduct()
        if include_optional:
            return LinkProduct(
                refreshed_at = '2023-02-16T09:14:11',
                last_attempted_at = '2023-02-16T09:14:11',
                error_code = 'rate_limit',
                error_message = '',
                unavailable = '',
                settings = moneykit.models.product_settings.ProductSettings(
                    required = True, 
                    prefetch = True, 
                    reason = 'display your account balances', )
            )
        else:
            return LinkProduct(
        )
        """

    def testLinkProduct(self):
        """Test LinkProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
