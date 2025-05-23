# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.product_state_changed_webhook import ProductStateChangedWebhook


class TestProductStateChangedWebhook(unittest.TestCase):
    """ProductStateChangedWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductStateChangedWebhook:
        """Test ProductStateChangedWebhook
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProductStateChangedWebhook`
        """
        model = ProductStateChangedWebhook()
        if include_optional:
            return ProductStateChangedWebhook(
                webhook_major_version = 1,
                webhook_minor_version = 0,
                webhook_idempotency_key = '',
                webhook_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                link_id = '',
                link_tags = [
                    ''
                    ],
                webhook_event = 'link.product_refresh',
                product = 'accounts',
                state = 'pending',
                state_changed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                error_message = ''
            )
        else:
            return ProductStateChangedWebhook(
                webhook_idempotency_key = '',
                webhook_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                link_id = '',
                link_tags = [
                    ''
                    ],
                product = 'accounts',
                state = 'pending',
                state_changed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testProductStateChangedWebhook(self):
        """Test ProductStateChangedWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
