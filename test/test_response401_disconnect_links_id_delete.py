# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.response401_disconnect_links_id_delete import (
    Response401DisconnectLinksIdDelete,
)


class TestResponse401DisconnectLinksIdDelete(unittest.TestCase):
    """Response401DisconnectLinksIdDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Response401DisconnectLinksIdDelete:
        """Test Response401DisconnectLinksIdDelete
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401DisconnectLinksIdDelete`
        """
        model = Response401DisconnectLinksIdDelete()
        if include_optional:
            return Response401DisconnectLinksIdDelete(
                error_code = link_error.unauthorized_access,
                error_message = None,
                documentation_url = None
            )
        else:
            return Response401DisconnectLinksIdDelete(
                error_message = None,
        )
        """

    def testResponse401DisconnectLinksIdDelete(self):
        """Test Response401DisconnectLinksIdDelete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
