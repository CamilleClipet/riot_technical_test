import base64


def encode_with_chosen_algo(payload):
    return base64.b64encode(payload)


def decode_with_chosen_algo(payload):
    return base64.b64decode(payload)
