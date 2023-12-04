# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.institution import Institution


class TestInstitution(unittest.TestCase):
    """Institution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Institution:
        """Test Institution
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Institution`
        """
        model = Institution()
        if include_optional:
            return Institution(
                institution_id = 'chase',
                institution_id_aliases = [
                    ''
                    ],
                name = 'Chase',
                country = 'US',
                domain = 'chase.com',
                color = '#0A89FF',
                color_dark = '#0A89FF',
                is_featured = True
            )
        else:
            return Institution(
                institution_id = 'chase',
                institution_id_aliases = [
                    ''
                    ],
                name = 'Chase',
                country = 'US',
                color = '#0A89FF',
                is_featured = True,
        )
        """

    def testInstitution(self):
        """Test Institution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()