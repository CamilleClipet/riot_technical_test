import hashlib
import hmac
import json
import os

from dotenv import load_dotenv

load_dotenv()


def compute_hmac_signature(payload: str) -> str:
    if not isinstance(payload, str):
        raise ValueError("Input must be a valid JSON string")
    cleaned_payload = json.dumps(
        json.loads(payload), separators=(",", ":"), sort_keys=True
    )
    payload_bytes = cleaned_payload.encode("utf-8")
    secret_key_bytes = os.getenv("SECRET_KEY").encode("utf-8")

    hmac_signature = hmac.new(secret_key_bytes, payload_bytes, hashlib.sha256)

    return hmac_signature.hexdigest()
