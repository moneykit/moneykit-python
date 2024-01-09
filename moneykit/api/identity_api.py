# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2023-02-18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501



from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr

from typing import List, Optional

from moneykit.models.identity_response import IdentityResponse

from moneykit.api_client import ApiClient
from moneykit.api_response import ApiResponse
from moneykit.rest import RESTResponseType


class IdentityApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_identities(
        self,
        id: Annotated[StrictStr, Field(description="The unique ID for this link.")],
        account_ids: Annotated[
            Optional[List[StrictStr]],
            Field(description="An optional list of account IDs to filter the results."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> IdentityResponse:
        """/links/{id}/identity

        Returns account owner information from the institution, including names, emails, phone     numbers, and addresses, for all permissioned accounts associated with a <a href=#tag/Links>link</a>.     <p>Some fields may be empty, if not provided by the institution.     <p>**Note** that this endpoint does **not** trigger a fetch of owner information from the institution; it merely returns     owner information that has already been fetched, either because `prefetch` was requested when the link was created,     or because of an on-demand update.  **To force a check for new/updated owner information, you must use the     <a href=#operation/refresh_products>/products</a> endpoint.**     <p>If you have requested prefetch or an on-demand update, you should check the `refreshed_at` date     for this product in the returned response, and compare that against the previous `refreshed_at` date, which you can     get from any previous response for this or any other account or link request.  If the refreshed_at date has not     increased, then updated data is not yet available.

        :param id: The unique ID for this link. (required)
        :type id: str
        :param account_ids: An optional list of account IDs to filter the results.
        :type account_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_identities_serialize(
            id=id,
            account_ids=account_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "IdentityResponse",
            "401": "Response401GetIdentitiesLinksIdIdentityGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "LinkErrorNotFoundResponse",
            "403": "LinkErrorForbiddenActionResponse",
            "410": "LinkErrorDeletedResponse",
            "422": "LinkErrorBadStateResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_identities_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="The unique ID for this link.")],
        account_ids: Annotated[
            Optional[List[StrictStr]],
            Field(description="An optional list of account IDs to filter the results."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[IdentityResponse]:
        """/links/{id}/identity

        Returns account owner information from the institution, including names, emails, phone     numbers, and addresses, for all permissioned accounts associated with a <a href=#tag/Links>link</a>.     <p>Some fields may be empty, if not provided by the institution.     <p>**Note** that this endpoint does **not** trigger a fetch of owner information from the institution; it merely returns     owner information that has already been fetched, either because `prefetch` was requested when the link was created,     or because of an on-demand update.  **To force a check for new/updated owner information, you must use the     <a href=#operation/refresh_products>/products</a> endpoint.**     <p>If you have requested prefetch or an on-demand update, you should check the `refreshed_at` date     for this product in the returned response, and compare that against the previous `refreshed_at` date, which you can     get from any previous response for this or any other account or link request.  If the refreshed_at date has not     increased, then updated data is not yet available.

        :param id: The unique ID for this link. (required)
        :type id: str
        :param account_ids: An optional list of account IDs to filter the results.
        :type account_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_identities_serialize(
            id=id,
            account_ids=account_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "IdentityResponse",
            "401": "Response401GetIdentitiesLinksIdIdentityGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "LinkErrorNotFoundResponse",
            "403": "LinkErrorForbiddenActionResponse",
            "410": "LinkErrorDeletedResponse",
            "422": "LinkErrorBadStateResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_identities_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="The unique ID for this link.")],
        account_ids: Annotated[
            Optional[List[StrictStr]],
            Field(description="An optional list of account IDs to filter the results."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """/links/{id}/identity

        Returns account owner information from the institution, including names, emails, phone     numbers, and addresses, for all permissioned accounts associated with a <a href=#tag/Links>link</a>.     <p>Some fields may be empty, if not provided by the institution.     <p>**Note** that this endpoint does **not** trigger a fetch of owner information from the institution; it merely returns     owner information that has already been fetched, either because `prefetch` was requested when the link was created,     or because of an on-demand update.  **To force a check for new/updated owner information, you must use the     <a href=#operation/refresh_products>/products</a> endpoint.**     <p>If you have requested prefetch or an on-demand update, you should check the `refreshed_at` date     for this product in the returned response, and compare that against the previous `refreshed_at` date, which you can     get from any previous response for this or any other account or link request.  If the refreshed_at date has not     increased, then updated data is not yet available.

        :param id: The unique ID for this link. (required)
        :type id: str
        :param account_ids: An optional list of account IDs to filter the results.
        :type account_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_identities_serialize(
            id=id,
            account_ids=account_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "IdentityResponse",
            "401": "Response401GetIdentitiesLinksIdIdentityGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "LinkErrorNotFoundResponse",
            "403": "LinkErrorForbiddenActionResponse",
            "410": "LinkErrorDeletedResponse",
            "422": "LinkErrorBadStateResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_identities_serialize(
        self,
        id,
        account_ids,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:
        _host = None

        _collection_formats: Dict[str, str] = {
            "account_ids": "multi",
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params["id"] = id
        # process the query parameters
        if account_ids is not None:
            _query_params.append(("account_ids", account_ids))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # authentication setting
        _auth_settings: List[str] = ["OAuth2ClientCredentials"]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/links/{id}/identity",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
