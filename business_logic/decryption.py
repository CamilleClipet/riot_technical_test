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

        # Try to decode as a tuple, if the value is a tuple,
        # reconstruct its original type
        try:
            decoded_tuple = json.loads(decoded_value)

            if (
                isinstance(decoded_tuple, list)
                and len(decoded_tuple) == 2
                and decoded_tuple[1] in ["int", "float", "bool", "NoneType"]
            ):
                val, typ = decoded_tuple
                if typ == "int":
                    dict_data[key] = int(val)
                if typ == "float":
                    dict_data[key] = float(val)
                elif typ == "bool":
                    dict_data[key] = bool(val)
                elif typ == "NoneType":
                    dict_data[key] = None
                else:
                    dict_data[key] = val
            else:
                dict_data[key] = (
                    decoded_tuple
                    if (
                        isinstance(decoded_tuple, list | dict)
                    )
                    else decoded_value
                )

        except json.JSONDecodeError:
            dict_data[key] = decoded_value

    return json.dumps(dict_data)
