# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.link_session_setting_overrides import LinkSessionSettingOverrides


class TestLinkSessionSettingOverrides(unittest.TestCase):
    """LinkSessionSettingOverrides unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkSessionSettingOverrides:
        """Test LinkSessionSettingOverrides
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkSessionSettingOverrides`
        """
        model = LinkSessionSettingOverrides()
        if include_optional:
            return LinkSessionSettingOverrides(
                providers = [
                    'moneykit'
                    ],
                link_permissions = moneykit.models.link_permissions.LinkPermissions(
                    requested = [
                        moneykit.models.requested_link_permission.RequestedLinkPermission(
                            scope = null, 
                            reason = 'display your account balances', 
                            required = True, )
                        ], ),
                products = moneykit.models.products_settings.ProductsSettings(
                    account_numbers = null, 
                    identity = null, 
                    transactions = null, 
                    investments = null, ),
                countries = [
                    'US'
                    ]
            )
        else:
            return LinkSessionSettingOverrides(
        )
        """

    def testLinkSessionSettingOverrides(self):
        """Test LinkSessionSettingOverrides"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()