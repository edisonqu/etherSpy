from twilio.rest import Client
from dotenv import load_dotenv
import os

def send_message(message):
    load_dotenv()

    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG06fe916a1774ad8ab365c4cf24946431',
        body=message,
        to= os.getenv("PHONE")
    )

    print(message.sid)