# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.app_client_response import AppClientResponse


class TestAppClientResponse(unittest.TestCase):
    """AppClientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppClientResponse:
        """Test AppClientResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AppClientResponse`
        """
        model = AppClientResponse()
        if include_optional:
            return AppClientResponse(
                client_id = 'live_5c739a369515e10fc9e0',
                client_name = 'My App (Prod)',
                scope = '',
                app = moneykit.models.app_response.AppResponse(
                    app_id = '3d18cdd1-fa96-4423-b781-bd5be036830e', 
                    name = 'My App', 
                    id = '3d18cdd1-fa96-4423-b781-bd5be036830e', 
                    app_name = 'My App', ),
                disabled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return AppClientResponse(
                client_id = 'live_5c739a369515e10fc9e0',
                client_name = 'My App (Prod)',
                scope = '',
                app = moneykit.models.app_response.AppResponse(
                    app_id = '3d18cdd1-fa96-4423-b781-bd5be036830e', 
                    name = 'My App', 
                    id = '3d18cdd1-fa96-4423-b781-bd5be036830e', 
                    app_name = 'My App', ),
        )
        """

    def testAppClientResponse(self):
        """Test AppClientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
