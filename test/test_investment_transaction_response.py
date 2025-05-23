# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.investment_transaction_response import (
    InvestmentTransactionResponse,
)


class TestInvestmentTransactionResponse(unittest.TestCase):
    """InvestmentTransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvestmentTransactionResponse:
        """Test InvestmentTransactionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InvestmentTransactionResponse`
        """
        model = InvestmentTransactionResponse()
        if include_optional:
            return InvestmentTransactionResponse(
                investment_transaction_id = '',
                account_id = '',
                amount = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                type = '',
                fees = '',
                forex_rate = '',
                price = '',
                quantity = '',
                security_id = ''
            )
        else:
            return InvestmentTransactionResponse(
                investment_transaction_id = '',
                account_id = '',
                amount = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                description = '',
                type = '',
        )
        """

    def testInvestmentTransactionResponse(self):
        """Test InvestmentTransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
