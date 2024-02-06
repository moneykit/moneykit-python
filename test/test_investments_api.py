# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moneykit.api.investments_api import InvestmentsApi


class TestInvestmentsApi(unittest.TestCase):
    """InvestmentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvestmentsApi()

    def tearDown(self) -> None:
        pass

    def test_get_holdings(self) -> None:
        """Test case for get_holdings

        /links/{id}/investments/holdings
        """
        pass

    def test_get_investment_transactions(self) -> None:
        """Test case for get_investment_transactions

        /links/{id}/investments/transactions
        """
        pass


if __name__ == "__main__":
    unittest.main()