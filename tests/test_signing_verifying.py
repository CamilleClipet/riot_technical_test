import pytest

from business_logic.signing import compute_hmac_signature
from business_logic.verifying import verify_signature


@pytest.mark.unit
def test_signing_with_valid_payload():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}' # noqa: E501
    signature = compute_hmac_signature(test_json)
    assert isinstance(signature, str)


@pytest.mark.unit
def test_signing_with_invalid_payload():
    test_json = {
        "name": "John",
        "children": ["Alice", "Charlie"],
        "profession": {"title": "Software Engineer", "years": 5},
        "isCadre": True,
        "address": None,
    }
    with pytest.raises(ValueError) as e:
        compute_hmac_signature(test_json)
    assert e.value.args[0] == "Input must be a valid JSON string"


@pytest.mark.unit
def test_verifying_is_valid():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}' # noqa: E501
    signature = compute_hmac_signature(test_json)
    is_signature_verified = verify_signature(signature, test_json)
    assert is_signature_verified is True


@pytest.mark.unit
def test_verifying_with_invalid_payload():
    test_json = {
        "name": "John",
        "children": ["Alice", "Charlie"],
        "profession": {"title": "Software Engineer", "years": 5},
        "isCadre": True,
        "address": None,
    }
    signature = "123456"
    with pytest.raises(ValueError) as e:
        verify_signature(signature, test_json)
    assert e.value.args[0] == "Input must be a valid JSON string"


@pytest.mark.unit
def test_verifying_with_wrong_signature():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}' # noqa: E501
    signature = compute_hmac_signature(test_json) + "1"
    is_signature_verified = verify_signature(signature, test_json)
    assert is_signature_verified is False


@pytest.mark.unit
def test_verifying_with_wrong_payload():
    test_json = '{"name": "John", "children": ["Alice", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}' # noqa: E501
    erroneous_test_json = '{"name": "John", "children": ["Alicia", "Charlie"], "profession": {"title": "Software Engineer", "years": 5}, "isCadre": true, "address": null}' # noqa: E501
    signature = compute_hmac_signature(erroneous_test_json)
    is_signature_verified = verify_signature(signature, test_json)
    assert is_signature_verified is False
