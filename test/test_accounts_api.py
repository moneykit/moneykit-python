# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.api.accounts_api import AccountsApi


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountsApi()

    def tearDown(self) -> None:
        pass

    def test_get_account(self) -> None:
        """Test case for get_account

        /links/{id}/accounts/{account_id}
        """
        pass

    def test_get_account_numbers(self) -> None:
        """Test case for get_account_numbers

        /links/{id}/accounts/numbers
        """
        pass

    def test_get_accounts(self) -> None:
        """Test case for get_accounts

        /links/{id}/accounts
        """
        pass

    def test_get_user_accounts(self) -> None:
        """Test case for get_user_accounts

        /users/{id}/accounts
        """
        pass


if __name__ == "__main__":
    unittest.main()