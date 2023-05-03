from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_auth_expired_access_token_response import APIErrorAuthExpiredAccessTokenResponse
from ...models.api_error_auth_unauthorized_response import APIErrorAuthUnauthorizedResponse
from ...models.get_user_accounts_response import GetUserAccountsResponse
from ...models.supported_version import SupportedVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, None, List[str]] = UNSET,
    institution_id: Union[Unset, None, List[str]] = UNSET,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Dict[str, Any]:
    url = "{}/users/{id}/accounts".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(moneykit_version, Unset) and moneykit_version is not None:
        headers["moneykit-version"] = str(moneykit_version)

    params: Dict[str, Any] = {}
    json_account_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(account_id, Unset):
        if account_id is None:
            json_account_id = None
        else:
            json_account_id = account_id

    params["account_id"] = json_account_id

    json_institution_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(institution_id, Unset):
        if institution_id is None:
            json_institution_id = None
        else:
            json_institution_id = institution_id

    params["institution_id"] = json_institution_id

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
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUserAccountsResponse.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
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
    account_id: Union[Unset, None, List[str]] = UNSET,
    institution_id: Union[Unset, None, List[str]] = UNSET,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
]:
    """/users/{id}/accounts

     Fetches all accounts belonging to a <a href=#operation/get_user_accounts>user</a>.

    Args:
        id (str): The unique ID for this user.  This is the same ID provided
                    in the call to <a href=#operation/create_link_session>/link-session</a> to create
            any link for this user.
        account_id (Union[Unset, None, List[str]]): If present, filters results to accounts
            matching the given IDs.
        institution_id (Union[Unset, None, List[str]]): If present, filters results to accounts at
            institutions matching the given IDs.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserAccountsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        account_id=account_id,
        institution_id=institution_id,
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
    account_id: Union[Unset, None, List[str]] = UNSET,
    institution_id: Union[Unset, None, List[str]] = UNSET,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
]:
    """/users/{id}/accounts

     Fetches all accounts belonging to a <a href=#operation/get_user_accounts>user</a>.

    Args:
        id (str): The unique ID for this user.  This is the same ID provided
                    in the call to <a href=#operation/create_link_session>/link-session</a> to create
            any link for this user.
        account_id (Union[Unset, None, List[str]]): If present, filters results to accounts
            matching the given IDs.
        institution_id (Union[Unset, None, List[str]]): If present, filters results to accounts at
            institutions matching the given IDs.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserAccountsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        account_id=account_id,
        institution_id=institution_id,
        moneykit_version=moneykit_version,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, None, List[str]] = UNSET,
    institution_id: Union[Unset, None, List[str]] = UNSET,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Response[
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
]:
    """/users/{id}/accounts

     Fetches all accounts belonging to a <a href=#operation/get_user_accounts>user</a>.

    Args:
        id (str): The unique ID for this user.  This is the same ID provided
                    in the call to <a href=#operation/create_link_session>/link-session</a> to create
            any link for this user.
        account_id (Union[Unset, None, List[str]]): If present, filters results to accounts
            matching the given IDs.
        institution_id (Union[Unset, None, List[str]]): If present, filters results to accounts at
            institutions matching the given IDs.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserAccountsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        account_id=account_id,
        institution_id=institution_id,
        moneykit_version=moneykit_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, None, List[str]] = UNSET,
    institution_id: Union[Unset, None, List[str]] = UNSET,
    moneykit_version: Union[Unset, None, SupportedVersion] = SupportedVersion.VALUE_0,
) -> Optional[
    Union[GetUserAccountsResponse, Union["APIErrorAuthExpiredAccessTokenResponse", "APIErrorAuthUnauthorizedResponse"]]
]:
    """/users/{id}/accounts

     Fetches all accounts belonging to a <a href=#operation/get_user_accounts>user</a>.

    Args:
        id (str): The unique ID for this user.  This is the same ID provided
                    in the call to <a href=#operation/create_link_session>/link-session</a> to create
            any link for this user.
        account_id (Union[Unset, None, List[str]]): If present, filters results to accounts
            matching the given IDs.
        institution_id (Union[Unset, None, List[str]]): If present, filters results to accounts at
            institutions matching the given IDs.
        moneykit_version (Union[Unset, None, SupportedVersion]): An enumeration. Default:
            SupportedVersion.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserAccountsResponse, Union['APIErrorAuthExpiredAccessTokenResponse', 'APIErrorAuthUnauthorizedResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            account_id=account_id,
            institution_id=institution_id,
            moneykit_version=moneykit_version,
        )
    ).parsed
