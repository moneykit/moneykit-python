# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.link_session_error_invalid_token_exchange import (
    LinkSessionErrorInvalidTokenExchange,
)


class TestLinkSessionErrorInvalidTokenExchange(unittest.TestCase):
    """LinkSessionErrorInvalidTokenExchange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkSessionErrorInvalidTokenExchange:
        """Test LinkSessionErrorInvalidTokenExchange
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkSessionErrorInvalidTokenExchange`
        """
        model = LinkSessionErrorInvalidTokenExchange()
        if include_optional:
            return LinkSessionErrorInvalidTokenExchange(
                error_code = 'link_session_error.invalid_token_exchange',
                error_message = 'Invalid token for link',
                documentation_url = ''
            )
        else:
            return LinkSessionErrorInvalidTokenExchange(
                error_message = 'Invalid token for link',
        )
        """

    def testLinkSessionErrorInvalidTokenExchange(self):
        """Test LinkSessionErrorInvalidTokenExchange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
