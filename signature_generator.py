import hashlib


def signature_func(amount, currency, id, secret_key):
    p = [str(amount), currency, id, secret_key]
    parametrs = ':'.join(p)
    return(hashlib.sha256(parametrs.encode('utf-8')).hexdigest())
