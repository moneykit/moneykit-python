# coding: utf-8

"""
    MoneyKit API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
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
from pydantic import StrictBool, StrictStr

from typing import Optional

from moneykit.models.get_institutions_response import GetInstitutionsResponse
from moneykit.models.institution import Institution

from moneykit.api_client import ApiClient
from moneykit.api_response import ApiResponse
from moneykit.rest import RESTResponseType


class InstitutionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_institution(
        self,
        institution_id: Annotated[
            StrictStr, Field(description="The institution ID to fetch.")
        ],
        moneykit_version: Optional[StrictStr] = None,
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
    ) -> Institution:
        """/institutions/{institution_id}

        Fetches details about a single institution.

        :param institution_id: The institution ID to fetch. (required)
        :type institution_id: str
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institution_serialize(
            institution_id=institution_id,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Institution",
            "401": "Response401GetInstitutionInstitutionsInstitutionIdGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "InstitutionErrorNotFoundResponse",
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
    def get_institution_with_http_info(
        self,
        institution_id: Annotated[
            StrictStr, Field(description="The institution ID to fetch.")
        ],
        moneykit_version: Optional[StrictStr] = None,
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
    ) -> ApiResponse[Institution]:
        """/institutions/{institution_id}

        Fetches details about a single institution.

        :param institution_id: The institution ID to fetch. (required)
        :type institution_id: str
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institution_serialize(
            institution_id=institution_id,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Institution",
            "401": "Response401GetInstitutionInstitutionsInstitutionIdGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "InstitutionErrorNotFoundResponse",
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
    def get_institution_without_preload_content(
        self,
        institution_id: Annotated[
            StrictStr, Field(description="The institution ID to fetch.")
        ],
        moneykit_version: Optional[StrictStr] = None,
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
        """/institutions/{institution_id}

        Fetches details about a single institution.

        :param institution_id: The institution ID to fetch. (required)
        :type institution_id: str
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institution_serialize(
            institution_id=institution_id,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Institution",
            "401": "Response401GetInstitutionInstitutionsInstitutionIdGet",
            "429": "APIErrorRateLimitExceededResponse",
            "404": "InstitutionErrorNotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_institution_serialize(
        self,
        institution_id,
        moneykit_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if institution_id is not None:
            _path_params["institution_id"] = institution_id
        # process the query parameters
        # process the header parameters
        if moneykit_version is not None:
            _header_params["moneykit-version"] = moneykit_version
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
            resource_path="/institutions/{institution_id}",
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

    @validate_call
    def get_institutions(
        self,
        name: Annotated[
            Optional[StrictStr],
            Field(
                description="If provided, returns only institutions containing this name (wholly or as a prefix)."
            ),
        ] = None,
        featured: Annotated[
            Optional[StrictBool],
            Field(description="If true, returns only featured institutions."),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description="A limit on the number of institutions to be returned."),
        ] = None,
        moneykit_version: Optional[StrictStr] = None,
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
    ) -> GetInstitutionsResponse:
        """/institutions

        Fetches a list of institutions, optionally filtered by name.  Results are paginated.

        :param name: If provided, returns only institutions containing this name (wholly or as a prefix).
        :type name: str
        :param featured: If true, returns only featured institutions.
        :type featured: bool
        :param cursor: Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)
        :type cursor: str
        :param limit: A limit on the number of institutions to be returned.
        :type limit: int
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institutions_serialize(
            name=name,
            featured=featured,
            cursor=cursor,
            limit=limit,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetInstitutionsResponse",
            "401": "Response401GetInstitutionsInstitutionsGet",
            "429": "APIErrorRateLimitExceededResponse",
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
    def get_institutions_with_http_info(
        self,
        name: Annotated[
            Optional[StrictStr],
            Field(
                description="If provided, returns only institutions containing this name (wholly or as a prefix)."
            ),
        ] = None,
        featured: Annotated[
            Optional[StrictBool],
            Field(description="If true, returns only featured institutions."),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description="A limit on the number of institutions to be returned."),
        ] = None,
        moneykit_version: Optional[StrictStr] = None,
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
    ) -> ApiResponse[GetInstitutionsResponse]:
        """/institutions

        Fetches a list of institutions, optionally filtered by name.  Results are paginated.

        :param name: If provided, returns only institutions containing this name (wholly or as a prefix).
        :type name: str
        :param featured: If true, returns only featured institutions.
        :type featured: bool
        :param cursor: Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)
        :type cursor: str
        :param limit: A limit on the number of institutions to be returned.
        :type limit: int
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institutions_serialize(
            name=name,
            featured=featured,
            cursor=cursor,
            limit=limit,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetInstitutionsResponse",
            "401": "Response401GetInstitutionsInstitutionsGet",
            "429": "APIErrorRateLimitExceededResponse",
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
    def get_institutions_without_preload_content(
        self,
        name: Annotated[
            Optional[StrictStr],
            Field(
                description="If provided, returns only institutions containing this name (wholly or as a prefix)."
            ),
        ] = None,
        featured: Annotated[
            Optional[StrictBool],
            Field(description="If true, returns only featured institutions."),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description="A limit on the number of institutions to be returned."),
        ] = None,
        moneykit_version: Optional[StrictStr] = None,
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
        """/institutions

        Fetches a list of institutions, optionally filtered by name.  Results are paginated.

        :param name: If provided, returns only institutions containing this name (wholly or as a prefix).
        :type name: str
        :param featured: If true, returns only featured institutions.
        :type featured: bool
        :param cursor: Cursor to fetch the next set of institutions. (You get this value from the previous call to `/institutions`.)
        :type cursor: str
        :param limit: A limit on the number of institutions to be returned.
        :type limit: int
        :param moneykit_version:
        :type moneykit_version: str
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

        _param = self._get_institutions_serialize(
            name=name,
            featured=featured,
            cursor=cursor,
            limit=limit,
            moneykit_version=moneykit_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetInstitutionsResponse",
            "401": "Response401GetInstitutionsInstitutionsGet",
            "429": "APIErrorRateLimitExceededResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_institutions_serialize(
        self,
        name,
        featured,
        cursor,
        limit,
        moneykit_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if name is not None:
            _query_params.append(("name", name))

        if featured is not None:
            _query_params.append(("featured", featured))

        if cursor is not None:
            _query_params.append(("cursor", cursor))

        if limit is not None:
            _query_params.append(("limit", limit))

        # process the header parameters
        if moneykit_version is not None:
            _header_params["moneykit-version"] = moneykit_version
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
            resource_path="/institutions",
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
