from business_logic.signing import compute_hmac_signature


def verify_signature(signature: str, payload: str) -> bool:
    if not isinstance(payload, str):
        raise ValueError("Input must be a valid JSON string")
    computed_signature = compute_hmac_signature(payload)
    return computed_signature == signature
