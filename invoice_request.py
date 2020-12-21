import requests
import json
from signature_generator import signature_func
import webbrowser


def invoice_request(variables):
    signature = signature_func(
        variables["order_amount"], variables["order_currency"], variables["order_id"], variables["secret_key"])

    url = "https://payop.com/v1/invoices/create"
    headers = {'Content-Type': 'application/json'}
    data = {
        "publicKey": variables["public_key"],
        "order": {
            "id": variables["order_id"],
            "amount": variables["order_amount"],
            "currency": variables["order_currency"],
            "items": [],
            "description": ""
        },
        "signature": signature,
        "payer": {
            "email": variables["email"],
            "phone": "",
            "name": ""
        },
        "language": "en",
        "resultUrl": "https://payop.com/",
        "failPath": "https://payop.com/",
    }

    req = requests.post(url, data=json.dumps(data), headers=headers)
    res = json.loads(req.text)

    if req.status_code == 200:
        invoice_id = res["data"]
        pay_url = f"https://payop.com/en/payment/invoice-preprocessing/{invoice_id}"
        webbrowser.open(pay_url)
    else:
        print(res["message"])
