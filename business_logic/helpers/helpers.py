import base64

# I have chosen to wrap the use of the base64 library in helper functions
# to make it easier to change the encoding/decoding algorithm in the future
# with minimal changes to the codebase


def encode_with_chosen_algo(payload: bytes) -> bytes:
    return base64.b64encode(payload)


def decode_with_chosen_algo(payload: bytes) -> bytes:
    return base64.b64decode(payload)


def type_as_string(value) -> str:
    return type(value).__name__
