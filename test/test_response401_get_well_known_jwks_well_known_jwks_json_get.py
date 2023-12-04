# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.response401_get_well_known_jwks_well_known_jwks_json_get import (
    Response401GetWellKnownJwksWellKnownJwksJsonGet,
)


class TestResponse401GetWellKnownJwksWellKnownJwksJsonGet(unittest.TestCase):
    """Response401GetWellKnownJwksWellKnownJwksJsonGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> Response401GetWellKnownJwksWellKnownJwksJsonGet:
        """Test Response401GetWellKnownJwksWellKnownJwksJsonGet
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401GetWellKnownJwksWellKnownJwksJsonGet`
        """
        model = Response401GetWellKnownJwksWellKnownJwksJsonGet()
        if include_optional:
            return Response401GetWellKnownJwksWellKnownJwksJsonGet(
                error_code = api_error.auth.unauthorized,
                error_message = Accounts access not permitted,
                documentation_url = None
            )
        else:
            return Response401GetWellKnownJwksWellKnownJwksJsonGet(
                error_message = Accounts access not permitted,
        )
        """

    def testResponse401GetWellKnownJwksWellKnownJwksJsonGet(self):
        """Test Response401GetWellKnownJwksWellKnownJwksJsonGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()