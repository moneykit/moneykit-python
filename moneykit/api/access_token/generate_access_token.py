from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.body_generate_access_token_auth_token_post import BodyGenerateAccessTokenAuthTokenPost
from ...models.generate_access_token_response import GenerateAccessTokenResponse
from ...models.supported_version import SupportedVersion
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: BodyGenerateAccessTokenAuthTokenPost,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/auth/token".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = GenerateAccessTokenResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = APIErrorAuthUnauthorizedResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = APIErrorAuthUnauthorizedResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: BodyGenerateAccessTokenAuthTokenPost,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    """/auth/token

     Create a new short-lived access token by validating your `client_id` and `client_secret`.

    The `access_token` is to be forwarded with all subsequent requests as
    `Authorization: Bearer {access_token}` HTTP header.

    When the token expires you must regenerate your `access_token`.

    The `client_id` and `client_secret` can be supplied as POST body parameters, or as a HTTP basic auth
    header.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
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
    form_data: BodyGenerateAccessTokenAuthTokenPost,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    """/auth/token

     Create a new short-lived access token by validating your `client_id` and `client_secret`.

    The `access_token` is to be forwarded with all subsequent requests as
    `Authorization: Bearer {access_token}` HTTP header.

    When the token expires you must regenerate your `access_token`.

    The `client_id` and `client_secret` can be supplied as POST body parameters, or as a HTTP basic auth
    header.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: BodyGenerateAccessTokenAuthTokenPost,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    """/auth/token

     Create a new short-lived access token by validating your `client_id` and `client_secret`.

    The `access_token` is to be forwarded with all subsequent requests as
    `Authorization: Bearer {access_token}` HTTP header.

    When the token expires you must regenerate your `access_token`.

    The `client_id` and `client_secret` can be supplied as POST body parameters, or as a HTTP basic auth
    header.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: BodyGenerateAccessTokenAuthTokenPost,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]]:
    """/auth/token

     Create a new short-lived access token by validating your `client_id` and `client_secret`.

    The `access_token` is to be forwarded with all subsequent requests as
    `Authorization: Bearer {access_token}` HTTP header.

    When the token expires you must regenerate your `access_token`.

    The `client_id` and `client_secret` can be supplied as POST body parameters, or as a HTTP basic auth
    header.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorAuthUnauthorizedResponse, GenerateAccessTokenResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            moneykit_version=moneykit_version,
        )
    ).parsed
