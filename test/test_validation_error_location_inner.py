# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.validation_error_location_inner import ValidationErrorLocationInner


class TestValidationErrorLocationInner(unittest.TestCase):
    """ValidationErrorLocationInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationErrorLocationInner:
        """Test ValidationErrorLocationInner
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ValidationErrorLocationInner`
        """
        model = ValidationErrorLocationInner()
        if include_optional:
            return ValidationErrorLocationInner(
            )
        else:
            return ValidationErrorLocationInner(
        )
        """

    def testValidationErrorLocationInner(self):
        """Test ValidationErrorLocationInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
