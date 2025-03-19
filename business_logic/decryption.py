import json

from business_logic.helpers.helpers import decode_with_chosen_algo


def decrypt(data: str) -> str:
    return decode_with_chosen_algo(data.encode("utf-8")).decode("utf-8")


def decrypt_json_depth_1(json_data: str) -> str:
    if not isinstance(json_data, str):
        raise ValueError("Input must be a valid JSON string")
    dict_data = json.loads(json_data)
    for key, value in dict_data.items():
        decoded_value = decrypt(value)
        if decoded_value == "null":
            dict_data[key] = None
        elif decoded_value == "True":
            dict_data[key] = True
        elif decoded_value == "False":
            dict_data[key] = False
        else:
            try:
                dict_data[key] = json.loads(decoded_value)
            except json.JSONDecodeError:
                dict_data[key] = decoded_value
    return json.dumps(dict_data)
