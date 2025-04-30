from uuid import uuid4
import moneykit
import moneykit.models
from auth import moneykit_client

link_session_api = moneykit.LinkSessionApi(moneykit_client())

response = link_session_api.create_link_session(
    moneykit.models.CreateLinkSessionRequest(
        customer_user=moneykit.models.CustomerUser(id=str(uuid4())),
        redirect_uri="http://localhost:3000",
    ),
)


link_session_token = response.link_session_token
print(link_session_token)