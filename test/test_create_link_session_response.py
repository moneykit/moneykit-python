# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.create_link_session_response import CreateLinkSessionResponse


class TestCreateLinkSessionResponse(unittest.TestCase):
    """CreateLinkSessionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateLinkSessionResponse:
        """Test CreateLinkSessionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateLinkSessionResponse`
        """
        model = CreateLinkSessionResponse()
        if include_optional:
            return CreateLinkSessionResponse(
                link_session_token = 'c7318ff7-257c-490e-8242-03a815b223b7'
            )
        else:
            return CreateLinkSessionResponse(
                link_session_token = 'c7318ff7-257c-490e-8242-03a815b223b7',
        )
        """

    def testCreateLinkSessionResponse(self):
        """Test CreateLinkSessionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
