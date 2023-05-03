from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_expired_access_token_response import APIErrorAuthExpiredAccessTokenResponse
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.api_error_rate_limit_exceeded_response import APIErrorRateLimitExceededResponse
from ...models.institution_error_not_found_response import InstitutionErrorNotFoundResponse
from ...models.institution_styling_response import InstitutionStylingResponse
from ...models.supported_version import SupportedVersion
from ...types import Response, Unset


def _get_kwargs(
    institution_id: str,
    *,
    client: AuthenticatedClient,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/institutions/{institution_id}/styling".format(client.base_url, institution_id=institution_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InstitutionStylingResponse.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = InstitutionErrorNotFoundResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
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
    institution_id: str,
    *,
    client: AuthenticatedClient,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions/{institution_id}/styling

     Fetches institution styling for a single institution.

    Args:
        institution_id (str): The institution ID to fetch.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, InstitutionErrorNotFoundResponse, InstitutionStylingResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        institution_id=institution_id,
        client=client,
        moneykit_version=moneykit_version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    institution_id: str,
    *,
    client: AuthenticatedClient,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions/{institution_id}/styling

     Fetches institution styling for a single institution.

    Args:
        institution_id (str): The institution ID to fetch.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, InstitutionErrorNotFoundResponse, InstitutionStylingResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return sync_detailed(
        institution_id=institution_id,
        client=client,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    institution_id: str,
    *,
    client: AuthenticatedClient,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions/{institution_id}/styling

     Fetches institution styling for a single institution.

    Args:
        institution_id (str): The institution ID to fetch.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, InstitutionErrorNotFoundResponse, InstitutionStylingResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        institution_id=institution_id,
        client=client,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    institution_id: str,
    *,
    client: AuthenticatedClient,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        InstitutionErrorNotFoundResponse,
        InstitutionStylingResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/institutions/{institution_id}/styling

     Fetches institution styling for a single institution.

    Args:
        institution_id (str): The institution ID to fetch.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, InstitutionErrorNotFoundResponse, InstitutionStylingResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return (
        await asyncio_detailed(
            institution_id=institution_id,
            client=client,
            moneykit_version=moneykit_version,
        )
    ).parsed
