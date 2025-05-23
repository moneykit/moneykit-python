# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.institution_error_not_found_response import (
    InstitutionErrorNotFoundResponse,
)


class TestInstitutionErrorNotFoundResponse(unittest.TestCase):
    """InstitutionErrorNotFoundResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstitutionErrorNotFoundResponse:
        """Test InstitutionErrorNotFoundResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InstitutionErrorNotFoundResponse`
        """
        model = InstitutionErrorNotFoundResponse()
        if include_optional:
            return InstitutionErrorNotFoundResponse(
                error_code = 'institution_error.not_found',
                error_message = 'Institution not found',
                documentation_url = ''
            )
        else:
            return InstitutionErrorNotFoundResponse(
        )
        """

    def testInstitutionErrorNotFoundResponse(self):
        """Test InstitutionErrorNotFoundResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
