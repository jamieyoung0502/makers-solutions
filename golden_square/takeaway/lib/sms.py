from lib.receipt import Receipt
import os
from dotenv import load_dotenv
# from twilio.rest import Client

class SMS:
    def __init__(self, receipt, twilio) -> None:
        if not isinstance(receipt, Receipt):
            raise ValueError("Only an instance of the Receipt class can be added")

        if not receipt.order.dishes:
            raise Exception("empty receipts are not valid")

        self._receipt = receipt
        self._twilio = twilio

    def send(self):
        load_dotenv()  # Load environment variables from the .env file

        # Account SID and Auth Token from console.twilio.com
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        from_num = os.environ.get('TWILIO_FROM_NUM')
        to_num = os.environ.get('TWILIO_TO_NUM')

        body = self._body_message()
        client = self._twilio(account_sid, auth_token)

        message = client.messages.create(
            to=to_num,
            from_=from_num,
            body=body)

        return message.sid

    def _body_message(self):
        body = f"\nThank you for your order! You ordered:\n"

        path = self._receipt.order.dishes
        for order in self._receipt.order.dishes.keys():
            plural = "s" if path[order]['quantity'] > 1 and order[-1] != 's' else ""
            body += f"{path[order]['quantity']} {order + plural} for £{path[order]['sum']}\n"

        body += "*" * 3
        body += "\n"
        body += f"For a total of: {self._receipt.grand_total()}\n"
        body += "*" * 3

        return body


