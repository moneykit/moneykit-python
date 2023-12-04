# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.models.get_user_links_response import GetUserLinksResponse


class TestGetUserLinksResponse(unittest.TestCase):
    """GetUserLinksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserLinksResponse:
        """Test GetUserLinksResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetUserLinksResponse`
        """
        model = GetUserLinksResponse()
        if include_optional:
            return GetUserLinksResponse(
                links = {
                    'key' : {link_id=mk_eqkWN34UEoa2NxyALG8pcV, institution_id=chase, institution_name=Chase, provider=mx, state=connected, last_synced_at=2023-02-16T09:14:11, tags=[user_type:admin], products={accounts={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11}, identity={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11, settings={required=true, prefetch=false}}}}
                    }
            )
        else:
            return GetUserLinksResponse(
                links = {
                    'key' : {link_id=mk_eqkWN34UEoa2NxyALG8pcV, institution_id=chase, institution_name=Chase, provider=mx, state=connected, last_synced_at=2023-02-16T09:14:11, tags=[user_type:admin], products={accounts={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11}, identity={refreshed_at=2023-02-16T09:14:11, last_attempted_at=2023-02-16T09:14:11, settings={required=true, prefetch=false}}}}
                    },
        )
        """

    def testGetUserLinksResponse(self):
        """Test GetUserLinksResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
