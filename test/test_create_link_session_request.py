# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.create_link_session_request import CreateLinkSessionRequest


class TestCreateLinkSessionRequest(unittest.TestCase):
    """CreateLinkSessionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateLinkSessionRequest:
        """Test CreateLinkSessionRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateLinkSessionRequest`
        """
        model = CreateLinkSessionRequest()
        if include_optional:
            return CreateLinkSessionRequest(
                settings = moneykit.models.link_session_setting_overrides.LinkSessionSettingOverrides(
                    providers = [
                        'moneykit'
                        ], 
                    link_permissions = null, 
                    products = null, 
                    countries = [
                        'US'
                        ], ),
                customer_user = moneykit.models.link_session_customer_user.LinkSessionCustomerUser(
                    id = 'z0123', 
                    email = null, 
                    phone = null, ),
                existing_link_id = 'mk_eqkWN34UEoa2NxyALG8pcV',
                institution_id = 'c7318ff7-257c-490e-8242-03a815b223b7',
                redirect_uri = 'https://yourdomain.com/oauth.html',
                webhook = 'https://yourdomain.com/moneykit_webhook',
                link_tags = [
                    ''
                    ],
                connect_features = moneykit.models.money_kit_connect_features.MoneyKitConnectFeatures(
                    issue_reporter = True, 
                    enable_money_id = True, )
            )
        else:
            return CreateLinkSessionRequest(
                customer_user = moneykit.models.link_session_customer_user.LinkSessionCustomerUser(
                    id = 'z0123', 
                    email = null, 
                    phone = null, ),
                redirect_uri = 'https://yourdomain.com/oauth.html',
        )
        """

    def testCreateLinkSessionRequest(self):
        """Test CreateLinkSessionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
