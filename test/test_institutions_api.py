# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.api.institutions_api import InstitutionsApi


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InstitutionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_institution(self) -> None:
        """Test case for get_institution

        /institutions/{institution_id}
        """
        pass

    def test_get_institutions(self) -> None:
        """Test case for get_institutions

        /institutions
        """
        pass


if __name__ == "__main__":
    unittest.main()
