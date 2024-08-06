# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.response401_refresh_products_links_id_products_post import (
    Response401RefreshProductsLinksIdProductsPost,
)


class TestResponse401RefreshProductsLinksIdProductsPost(unittest.TestCase):
    """Response401RefreshProductsLinksIdProductsPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> Response401RefreshProductsLinksIdProductsPost:
        """Test Response401RefreshProductsLinksIdProductsPost
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Response401RefreshProductsLinksIdProductsPost`
        """
        model = Response401RefreshProductsLinksIdProductsPost()
        if include_optional:
            return Response401RefreshProductsLinksIdProductsPost(
                error_code = link_error.unauthorized_access,
                error_message = None,
                documentation_url = None
            )
        else:
            return Response401RefreshProductsLinksIdProductsPost(
                error_message = None,
        )
        """

    def testResponse401RefreshProductsLinksIdProductsPost(self):
        """Test Response401RefreshProductsLinksIdProductsPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
