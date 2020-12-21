from invoice_request import invoice_request

variables = {
    "public_key": "application-12345",
    "secret_key": "0123456789",
    "order_id": "test_transaction",
    "order_amount": 20,
    "order_currency": "USD",
    "email": "youremail@gmail.com"
}

invoice_request(variables)
