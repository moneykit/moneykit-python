# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.transaction_sync import TransactionSync


class TestTransactionSync(unittest.TestCase):
    """TransactionSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSync:
        """Test TransactionSync
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionSync`
        """
        model = TransactionSync()
        if include_optional:
            return TransactionSync(
                created = [
                    moneykit.models.transaction_response.TransactionResponse(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = '', 
                        enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                            category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                value = 'food_and_drink', 
                                confidence = 99, ), 
                            subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                value = 'coffee', 
                                confidence = 99, ), 
                            merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Starbucks', 
                                logo = 'https://example.com/starbucks.png', 
                                confidence = 99, ), 
                            processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Square', 
                                logo = 'https://example.com/square.png', 
                                confidence = 99, ), 
                            recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                frequency = 'monthly', 
                                next_predicted_date = '2024-08-03', ), ), 
                        original_id = '', )
                    ],
                updated = [
                    moneykit.models.transaction_response.TransactionResponse(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = '', 
                        enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                            category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                value = 'food_and_drink', 
                                confidence = 99, ), 
                            subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                value = 'coffee', 
                                confidence = 99, ), 
                            merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Starbucks', 
                                logo = 'https://example.com/starbucks.png', 
                                confidence = 99, ), 
                            processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Square', 
                                logo = 'https://example.com/square.png', 
                                confidence = 99, ), 
                            recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                frequency = 'monthly', 
                                next_predicted_date = '2024-08-03', ), ), 
                        original_id = '', )
                    ],
                removed = [
                    ''
                    ]
            )
        else:
            return TransactionSync(
                created = [
                    moneykit.models.transaction_response.TransactionResponse(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = '', 
                        enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                            category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                value = 'food_and_drink', 
                                confidence = 99, ), 
                            subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                value = 'coffee', 
                                confidence = 99, ), 
                            merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Starbucks', 
                                logo = 'https://example.com/starbucks.png', 
                                confidence = 99, ), 
                            processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Square', 
                                logo = 'https://example.com/square.png', 
                                confidence = 99, ), 
                            recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                frequency = 'monthly', 
                                next_predicted_date = '2024-08-03', ), ), 
                        original_id = '', )
                    ],
                updated = [
                    moneykit.models.transaction_response.TransactionResponse(
                        transaction_id = 'c7318ff7-257c-490e-8242-03a815b223b7', 
                        account_id = 'acc_6Tef269B6ZArSVpYrxtjBV', 
                        amount = '384.05', 
                        type = debit, 
                        currency = 'USD', 
                        date = '2023-02-16T00:00:00', 
                        datetime = '2023-02-16T09:14:11', 
                        description = 'Regina's Mulberry', 
                        raw_description = 'Regina's Mulberry #1402 T48999-84', 
                        pending = True, 
                        category = '', 
                        enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                            category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                value = 'food_and_drink', 
                                confidence = 99, ), 
                            subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                value = 'coffee', 
                                confidence = 99, ), 
                            merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Starbucks', 
                                logo = 'https://example.com/starbucks.png', 
                                confidence = 99, ), 
                            processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                id = 'a0822a4f-a59b-4fc9-a768-d880da5bd090', 
                                name = 'Square', 
                                logo = 'https://example.com/square.png', 
                                confidence = 99, ), 
                            recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                frequency = 'monthly', 
                                next_predicted_date = '2024-08-03', ), ), 
                        original_id = '', )
                    ],
                removed = [
                    ''
                    ],
        )
        """

    def testTransactionSync(self):
        """Test TransactionSync"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
