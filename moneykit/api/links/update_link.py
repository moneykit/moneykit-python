from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_expired_access_token_response import APIErrorAuthExpiredAccessTokenResponse
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.api_error_rate_limit_exceeded_response import APIErrorRateLimitExceededResponse
from ...models.link_error_bad_state_response import LinkErrorBadStateResponse
from ...models.link_error_deleted_response import LinkErrorDeletedResponse
from ...models.link_error_forbidden_action_response import LinkErrorForbiddenActionResponse
from ...models.link_error_not_found_response import LinkErrorNotFoundResponse
from ...models.link_error_unauthorized_access_response import LinkErrorUnauthorizedAccessResponse
from ...models.link_response import LinkResponse
from ...models.supported_version import SupportedVersion
from ...models.update_link_request import UpdateLinkRequest
from ...types import Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLinkRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/links/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
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
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LinkResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:

        def _parse_response_401(
            data: object,
        ) -> Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_0 = APIErrorAuthExpiredAccessTokenResponse.from_dict(data)

                return response_401_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_1 = APIErrorAuthUnauthorizedResponse.from_dict(data)

                return response_401_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_401_type_2 = LinkErrorUnauthorizedAccessResponse.from_dict(data)

            return response_401_type_2

        response_401 = _parse_response_401(response.json())

        return response_401
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = APIErrorRateLimitExceededResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = LinkErrorNotFoundResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LinkErrorForbiddenActionResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.GONE:
        response_410 = LinkErrorDeletedResponse.from_dict(response.json())

        return response_410
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = LinkErrorBadStateResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLinkRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    """/links/{id}

     Updates the link configuration.

    Args:
        id (str): The unique ID for this link.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (UpdateLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, LinkErrorBadStateResponse, LinkErrorDeletedResponse, LinkErrorForbiddenActionResponse, LinkErrorNotFoundResponse, LinkResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse', 'LinkErrorUnauthorizedAccessResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLinkRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    """/links/{id}

     Updates the link configuration.

    Args:
        id (str): The unique ID for this link.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (UpdateLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, LinkErrorBadStateResponse, LinkErrorDeletedResponse, LinkErrorForbiddenActionResponse, LinkErrorNotFoundResponse, LinkResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse', 'LinkErrorUnauthorizedAccessResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLinkRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    """/links/{id}

     Updates the link configuration.

    Args:
        id (str): The unique ID for this link.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (UpdateLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIErrorRateLimitExceededResponse, LinkErrorBadStateResponse, LinkErrorDeletedResponse, LinkErrorForbiddenActionResponse, LinkErrorNotFoundResponse, LinkResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse', 'LinkErrorUnauthorizedAccessResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLinkRequest,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[
        APIErrorRateLimitExceededResponse,
        LinkErrorBadStateResponse,
        LinkErrorDeletedResponse,
        LinkErrorForbiddenActionResponse,
        LinkErrorNotFoundResponse,
        LinkResponse,
        Union[
            "APIErrorAuthExpiredAccessTokenResponse",
            "APIErrorAuthUnauthorizedResponse",
            "LinkErrorUnauthorizedAccessResponse",
        ],
    ]
]:
    """/links/{id}

     Updates the link configuration.

    Args:
        id (str): The unique ID for this link.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.
        json_body (UpdateLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIErrorRateLimitExceededResponse, LinkErrorBadStateResponse, LinkErrorDeletedResponse, LinkErrorForbiddenActionResponse, LinkErrorNotFoundResponse, LinkResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse', 'LinkErrorUnauthorizedAccessResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            moneykit_version=moneykit_version,
        )
    ).parsed
