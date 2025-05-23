# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.basic_account_details import BasicAccountDetails


class TestBasicAccountDetails(unittest.TestCase):
    """BasicAccountDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BasicAccountDetails:
        """Test BasicAccountDetails
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BasicAccountDetails`
        """
        model = BasicAccountDetails()
        if include_optional:
            return BasicAccountDetails(
                name = '',
                last_synced_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                institution_id = '',
                link_id = ''
            )
        else:
            return BasicAccountDetails(
                name = '',
                institution_id = '',
                link_id = '',
        )
        """

    def testBasicAccountDetails(self):
        """Test BasicAccountDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
