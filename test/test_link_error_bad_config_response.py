# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.link_error_bad_config_response import LinkErrorBadConfigResponse


class TestLinkErrorBadConfigResponse(unittest.TestCase):
    """LinkErrorBadConfigResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkErrorBadConfigResponse:
        """Test LinkErrorBadConfigResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkErrorBadConfigResponse`
        """
        model = LinkErrorBadConfigResponse()
        if include_optional:
            return LinkErrorBadConfigResponse(
                error_code = 'link_error.bad_config',
                error_message = '',
                documentation_url = ''
            )
        else:
            return LinkErrorBadConfigResponse(
                error_message = '',
        )
        """

    def testLinkErrorBadConfigResponse(self):
        """Test LinkErrorBadConfigResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
