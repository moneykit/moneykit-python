from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_expired_access_token_response import APIErrorAuthExpiredAccessTokenResponse
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.api_error_rate_limit_exceeded_response import APIErrorRateLimitExceededResponse
from ...models.get_institutions_response import GetInstitutionsResponse
from ...models.supported_version import SupportedVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    featured: Union[Unset, None, bool] = False,
    cursor: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/institutions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    params: Dict[str, Any] = {}
    params["name"] = name

    params["featured"] = featured

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInstitutionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:

        def _parse_response_401(
            data: object,
        ) -> Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_0 = APIErrorAuthExpiredAccessTokenResponse.from_dict(data)

                return response_401_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_401_type_1 = APIErrorAuthUnauthorizedResponse.from_dict(data)

            return response_401_type_1

        response_401 = _parse_response_401(response.json())

        return response_401
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = APIErrorRateLimitExceededResponse.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    featured: Union[Unset, None, bool] = False,
    cursor: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions

     Fetches a list of institutions, optionally filtered by name.  Results are paginated.

    Args:
        name (Union[Unset, None, str]): If provided, returns only institutions containing this
            name (wholly or as a prefix).
        featured (Union[Unset, None, bool]): If true, returns only featured institutions.
        cursor (Union[Unset, None, str]): Cursor to fetch the next set of institutions. (You get
            this value from the previous call to `/institutions`.)
        limit (Union[Unset, None, int]): A limit on the number of institutions to be returned.
            Default: 50.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, GetInstitutionsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        featured=featured,
        cursor=cursor,
        limit=limit,
        moneykit_version=moneykit_version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    featured: Union[Unset, None, bool] = False,
    cursor: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions

     Fetches a list of institutions, optionally filtered by name.  Results are paginated.

    Args:
        name (Union[Unset, None, str]): If provided, returns only institutions containing this
            name (wholly or as a prefix).
        featured (Union[Unset, None, bool]): If true, returns only featured institutions.
        cursor (Union[Unset, None, str]): Cursor to fetch the next set of institutions. (You get
            this value from the previous call to `/institutions`.)
        limit (Union[Unset, None, int]): A limit on the number of institutions to be returned.
            Default: 50.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, GetInstitutionsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return sync_detailed(
        client=client,
        name=name,
        featured=featured,
        cursor=cursor,
        limit=limit,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    featured: Union[Unset, None, bool] = False,
    cursor: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions

     Fetches a list of institutions, optionally filtered by name.  Results are paginated.

    Args:
        name (Union[Unset, None, str]): If provided, returns only institutions containing this
            name (wholly or as a prefix).
        featured (Union[Unset, None, bool]): If true, returns only featured institutions.
        cursor (Union[Unset, None, str]): Cursor to fetch the next set of institutions. (You get
            this value from the previous call to `/institutions`.)
        limit (Union[Unset, None, int]): A limit on the number of institutions to be returned.
            Default: 50.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, GetInstitutionsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        featured=featured,
        cursor=cursor,
        limit=limit,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    featured: Union[Unset, None, bool] = False,
    cursor: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        GetInstitutionsResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions

     Fetches a list of institutions, optionally filtered by name.  Results are paginated.

    Args:
        name (Union[Unset, None, str]): If provided, returns only institutions containing this
            name (wholly or as a prefix).
        featured (Union[Unset, None, bool]): If true, returns only featured institutions.
        cursor (Union[Unset, None, str]): Cursor to fetch the next set of institutions. (You get
            this value from the previous call to `/institutions`.)
        limit (Union[Unset, None, int]): A limit on the number of institutions to be returned.
            Default: 50.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, GetInstitutionsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            featured=featured,
            cursor=cursor,
            limit=limit,
            moneykit_version=moneykit_version,
        )
    ).parsed
