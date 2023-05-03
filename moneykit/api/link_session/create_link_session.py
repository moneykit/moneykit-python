from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_expired_access_token_response import APIErrorAuthExpiredAccessTokenResponse
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.create_link_session_request import CreateLinkSessionRequest
from ...models.create_link_session_response import CreateLinkSessionResponse
from ...models.link_session_error_forbidden_config_response import LinkSessionErrorForbiddenConfigResponse
from ...models.supported_version import SupportedVersion
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreateLinkSessionRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/link-session".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateLinkSessionResponse.from_dict(response.json())

        return response_201
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
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LinkSessionErrorForbiddenConfigResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
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
    json_body: CreateLinkSessionRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/link-session

     This endpoint is to be called by your back end, to establish a new link session
            for creating a link to your end user's institution.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (CreateLinkSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateLinkSessionResponse, LinkSessionErrorForbiddenConfigResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: CreateLinkSessionRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/link-session

     This endpoint is to be called by your back end, to establish a new link session
            for creating a link to your end user's institution.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (CreateLinkSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateLinkSessionResponse, LinkSessionErrorForbiddenConfigResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateLinkSessionRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/link-session

     This endpoint is to be called by your back end, to establish a new link session
            for creating a link to your end user's institution.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (CreateLinkSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateLinkSessionResponse, LinkSessionErrorForbiddenConfigResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateLinkSessionRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        CreateLinkSessionResponse,
        LinkSessionErrorForbiddenConfigResponse,
        Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"],
    ]
]:
    """/link-session

     This endpoint is to be called by your back end, to establish a new link session
            for creating a link to your end user's institution.

    Args:
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (CreateLinkSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateLinkSessionResponse, LinkSessionErrorForbiddenConfigResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            moneykit_version=moneykit_version,
        )
    ).parsed
