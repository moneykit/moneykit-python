# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.eft_number import EftNumber


class TestEftNumber(unittest.TestCase):
    """EftNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EftNumber:
        """Test EftNumber
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EftNumber`
        """
        model = EftNumber()
        if include_optional:
            return EftNumber(
                account_number = '',
                institution_number = '',
                branch_number = ''
            )
        else:
            return EftNumber(
                account_number = '',
                institution_number = '',
                branch_number = '',
        )
        """

    def testEftNumber(self):
        """Test EftNumber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
