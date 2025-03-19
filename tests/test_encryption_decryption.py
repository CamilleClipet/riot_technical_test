import json

import pytest

from business_logic.decryption import decrypt, decrypt_json_depth_1
from business_logic.encryption import encrypt, encrypt_json_depth_1


@pytest.mark.unit
def test_string_encryption_decryption():
    test_string = "Hello World"
    encrypted_string = encrypt(test_string)
    decrypted_string = decrypt(encrypted_string)
    assert test_string == decrypted_string


@pytest.mark.unit
def test_json_encryption():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}'
    encrypted_json = encrypt_json_depth_1(test_json)
    encrypted_json_as_dict = json.loads(encrypted_json)
    for key, _value in encrypted_json_as_dict.items():
        assert isinstance(encrypted_json_as_dict[key], str) is True


@pytest.mark.unit
def test_json_encryption_decryption():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}'
    encrypted_json = encrypt_json_depth_1(test_json)
    decrypted_json = decrypt_json_depth_1(encrypted_json)
    assert test_json == decrypted_json
