import os
import moneykit
import moneykit.models
from moneykit.rest import ApiException


def moneykit_client() -> moneykit.ApiClient:
    # Defaults to MoneyKit-Version: 2023-02-18
    config = moneykit.Configuration(host="https://api.moneykit.com")
    api_client = moneykit.ApiClient(config)
    try:
        access_token_api = moneykit.AccessTokenApi(api_client)
        response = access_token_api.create_access_token(
            client_id=os.environ["MONEYKIT_CLIENT_ID"],
            client_secret=os.environ["MONEYKIT_CLIENT_SECRET"],
            grant_type="client_credentials",
        )

        api_client.configuration.access_token = response.access_token
        return api_client
    except ApiException as e:
        print("Exception when calling AccessTokenApi.create_access_token: %s\n" % e)


print(moneykit_client().configuration.access_token)
