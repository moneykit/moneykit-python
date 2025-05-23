# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.link_error_unauthorized_access_response import (
    LinkErrorUnauthorizedAccessResponse,
)


class TestLinkErrorUnauthorizedAccessResponse(unittest.TestCase):
    """LinkErrorUnauthorizedAccessResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkErrorUnauthorizedAccessResponse:
        """Test LinkErrorUnauthorizedAccessResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkErrorUnauthorizedAccessResponse`
        """
        model = LinkErrorUnauthorizedAccessResponse()
        if include_optional:
            return LinkErrorUnauthorizedAccessResponse(
                error_code = 'link_error.unauthorized_access',
                error_message = 'Unauthorized link access.',
                documentation_url = ''
            )
        else:
            return LinkErrorUnauthorizedAccessResponse(
        )
        """

    def testLinkErrorUnauthorizedAccessResponse(self):
        """Test LinkErrorUnauthorizedAccessResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
