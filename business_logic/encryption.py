import json

from business_logic.helpers.helpers import encode_with_chosen_algo


def encrypt(data: str) -> str:
    return encode_with_chosen_algo(data.encode("utf-8")).decode("utf-8")


def encrypt_bool(value: bool) -> str:
    return encrypt("True" if value else "False")


def encrypt_null() -> str:
    return encrypt("null")


def encrypt_json_item(value) -> str:
    if isinstance(value, (dict | list)):
        json_str = json.dumps(value)
        return encrypt(json_str)
    elif isinstance(value, (int | float | str)):
        return encrypt(str(value))
    elif value is None:
        return encrypt_null()
    elif isinstance(value, bool):
        return encrypt_bool(value)
    else:
        raise ValueError("Unsupported data type")


def encrypt_json_depth_1(json_data: str) -> str:
    if not isinstance(json_data, str):
        raise ValueError("Input must be a valid JSON string")
    dict_data = json.loads(json_data)
    for key, value in dict_data.items():
        dict_data[key] = encrypt_json_item(value)
    return json.dumps(dict_data)
