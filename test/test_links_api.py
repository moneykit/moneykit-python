# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.api.links_api import LinksApi


class TestLinksApi(unittest.TestCase):
    """LinksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LinksApi()

    def tearDown(self) -> None:
        pass

    def test_delete_link(self) -> None:
        """Test case for delete_link

        /links/{id}
        """
        pass

    def test_get_link(self) -> None:
        """Test case for get_link

        /links/{id}
        """
        pass

    def test_get_links(self) -> None:
        """Test case for get_links

        /links
        """
        pass

    def test_get_user_links(self) -> None:
        """Test case for get_user_links

        /users/{id}/links
        """
        pass

    def test_import_link(self) -> None:
        """Test case for import_link

        /links/import
        """
        pass

    def test_import_transactions(self) -> None:
        """Test case for import_transactions

        /links/{id}/import/transactions
        """
        pass

    def test_reset_link(self) -> None:
        """Test case for reset_link

        /links/{id}/reset
        """
        pass

    def test_update_link(self) -> None:
        """Test case for update_link

        /links/{id}
        """
        pass


if __name__ == "__main__":
    unittest.main()
