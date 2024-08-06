# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.response_handle_link_webhook_event_request_body_webhook_post import (
    ResponseHandleLinkWebhookEventRequestBodyWebhookPost,
)


class TestResponseHandleLinkWebhookEventRequestBodyWebhookPost(unittest.TestCase):
    """ResponseHandleLinkWebhookEventRequestBodyWebhookPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ResponseHandleLinkWebhookEventRequestBodyWebhookPost:
        """Test ResponseHandleLinkWebhookEventRequestBodyWebhookPost
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseHandleLinkWebhookEventRequestBodyWebhookPost`
        """
        model = ResponseHandleLinkWebhookEventRequestBodyWebhookPost()
        if include_optional:
            return ResponseHandleLinkWebhookEventRequestBodyWebhookPost(
                webhook_event = transactions.updates_available,
                webhook_major_version = 1,
                webhook_minor_version = 0,
                webhook_idempotency_key = None,
                webhook_timestamp = None,
                link_id = None,
                link_tags = None,
                state = 'completed',
                error = 'system_error',
                error_message = None,
                product = 'accounts',
                state_changed_at = None,
                has_history = None
            )
        else:
            return ResponseHandleLinkWebhookEventRequestBodyWebhookPost(
                webhook_idempotency_key = None,
                webhook_timestamp = None,
                link_id = None,
                link_tags = None,
                state = 'completed',
                product = 'accounts',
                state_changed_at = None,
                has_history = None,
        )
        """

    def testResponseHandleLinkWebhookEventRequestBodyWebhookPost(self):
        """Test ResponseHandleLinkWebhookEventRequestBodyWebhookPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
