import json

from business_logic.signing import compute_hmac_signature


def verify_signature(signature: str, payload: str) -> bool:
    if not isinstance(payload, str):
        raise ValueError("Input must be a valid JSON string")
    cleaned_payload = json.dumps(
        json.loads(payload), separators=(",", ":"), sort_keys=True
    )
    computed_signature = compute_hmac_signature(cleaned_payload)
    return computed_signature == signature
