# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.link_error_bad_state_response import LinkErrorBadStateResponse


class TestLinkErrorBadStateResponse(unittest.TestCase):
    """LinkErrorBadStateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkErrorBadStateResponse:
        """Test LinkErrorBadStateResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkErrorBadStateResponse`
        """
        model = LinkErrorBadStateResponse()
        if include_optional:
            return LinkErrorBadStateResponse(
                error_code = 'link_error.bad_state',
                error_message = '',
                documentation_url = '',
                link_error_code = ''
            )
        else:
            return LinkErrorBadStateResponse(
                error_message = '',
                link_error_code = '',
        )
        """

    def testLinkErrorBadStateResponse(self):
        """Test LinkErrorBadStateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()