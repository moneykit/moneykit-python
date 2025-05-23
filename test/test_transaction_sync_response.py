# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from moneykit.models.transaction_sync_response import TransactionSyncResponse


class TestTransactionSyncResponse(unittest.TestCase):
    """TransactionSyncResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSyncResponse:
        """Test TransactionSyncResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionSyncResponse`
        """
        model = TransactionSyncResponse()
        if include_optional:
            return TransactionSyncResponse(
                transactions = moneykit.models.transaction_sync.TransactionSync(
                    created = [
                        moneykit.models.transaction_response.TransactionResponse(
                            transaction_id = '', 
                            account_id = '', 
                            amount = '', 
                            type = null, 
                            currency = '', 
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            raw_description = '', 
                            pending = True, 
                            category = '', 
                            enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                                category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                    value = '', 
                                    confidence = 56, ), 
                                subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                    value = '', 
                                    confidence = 56, ), 
                                merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                    id = '', 
                                    name = '', 
                                    logo = '', 
                                    confidence = 56, ), 
                                processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                    id = '', 
                                    name = '', 
                                    logo = '', 
                                    confidence = 56, ), 
                                recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                    frequency = '', 
                                    next_predicted_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ), ), 
                            original_id = '', )
                        ], 
                    updated = [
                        moneykit.models.transaction_response.TransactionResponse(
                            transaction_id = '', 
                            account_id = '', 
                            amount = '', 
                            type = null, 
                            currency = '', 
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            raw_description = '', 
                            pending = True, 
                            original_id = '', )
                        ], 
                    removed = [
                        ''
                        ], ),
                accounts = [
                    moneykit.models.account_response.AccountResponse(
                        account_id = '', 
                        account_type = '', 
                        name = '', 
                        nickname = '', 
                        account_mask = '', 
                        balances = null, 
                        original_id = '', 
                        closed = True, )
                    ],
                cursor = moneykit.models.cursor_pagination.CursorPagination(
                    next = '', ),
                has_more = True,
                link = moneykit.models.link_common.LinkCommon(
                    link_id = '', 
                    institution_id = '', 
                    institution_name = '', 
                    institution_avatar = '', 
                    state = null, 
                    error_code = null, 
                    last_synced_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    provider = null, 
                    link_tags = [
                        ''
                        ], 
                    tags = [
                        ''
                        ], 
                    webhook = '', 
                    products = null, 
                    available_products = [
                        'accounts'
                        ], )
            )
        else:
            return TransactionSyncResponse(
                transactions = moneykit.models.transaction_sync.TransactionSync(
                    created = [
                        moneykit.models.transaction_response.TransactionResponse(
                            transaction_id = '', 
                            account_id = '', 
                            amount = '', 
                            type = null, 
                            currency = '', 
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            raw_description = '', 
                            pending = True, 
                            category = '', 
                            enrichment = moneykit.models.transaction_enrichment_response.TransactionEnrichmentResponse(
                                category = moneykit.models.transaction_category_response.TransactionCategoryResponse(
                                    value = '', 
                                    confidence = 56, ), 
                                subcategory = moneykit.models.transaction_subcategory_response.TransactionSubcategoryResponse(
                                    value = '', 
                                    confidence = 56, ), 
                                merchant = moneykit.models.transaction_merchant_response.TransactionMerchantResponse(
                                    id = '', 
                                    name = '', 
                                    logo = '', 
                                    confidence = 56, ), 
                                processor = moneykit.models.transaction_processor_response.TransactionProcessorResponse(
                                    id = '', 
                                    name = '', 
                                    logo = '', 
                                    confidence = 56, ), 
                                recurrence = moneykit.models.transaction_recurrence_response.TransactionRecurrenceResponse(
                                    frequency = '', 
                                    next_predicted_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ), ), 
                            original_id = '', )
                        ], 
                    updated = [
                        moneykit.models.transaction_response.TransactionResponse(
                            transaction_id = '', 
                            account_id = '', 
                            amount = '', 
                            type = null, 
                            currency = '', 
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            raw_description = '', 
                            pending = True, 
                            original_id = '', )
                        ], 
                    removed = [
                        ''
                        ], ),
                accounts = [
                    moneykit.models.account_response.AccountResponse(
                        account_id = '', 
                        account_type = '', 
                        name = '', 
                        nickname = '', 
                        account_mask = '', 
                        balances = null, 
                        original_id = '', 
                        closed = True, )
                    ],
                cursor = moneykit.models.cursor_pagination.CursorPagination(
                    next = '', ),
                has_more = True,
                link = moneykit.models.link_common.LinkCommon(
                    link_id = '', 
                    institution_id = '', 
                    institution_name = '', 
                    institution_avatar = '', 
                    state = null, 
                    error_code = null, 
                    last_synced_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    provider = null, 
                    link_tags = [
                        ''
                        ], 
                    tags = [
                        ''
                        ], 
                    webhook = '', 
                    products = null, 
                    available_products = [
                        'accounts'
                        ], ),
        )
        """

    def testTransactionSyncResponse(self):
        """Test TransactionSyncResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
