from flask import Flask, Response, request
import json

from business_logic.decryption import decrypt_json_depth_1
from business_logic.encryption import encrypt_json_depth_1
from business_logic.signing import compute_hmac_signature
from business_logic.verifying import verify_signature

app = Flask(__name__)


@app.route("/encrypt", methods=["POST"])
def _encrypt() -> Response:
    raw_data = request.data
    if raw_data is None:
        return Response("Bad Request", status=400)

    try:
        json_data = raw_data.decode("utf-8")
        result = encrypt_json_depth_1(json_data)
        return Response(result, status=200)

    except Exception as e:
        return Response(str(e), status=500)


@app.route("/decrypt", methods=["POST"])
def _decrypt() -> Response:
    raw_data = request.data
    if raw_data is None:
        return Response("Bad Request", status=400)
    try:
        json_data = raw_data.decode("utf-8")
        result = decrypt_json_depth_1(json_data)
        return Response(result, status=200)
    except Exception as e:
        return Response(str(e), status=500)


@app.route("/sign", methods=["POST"])
def _sign():
    raw_data = request.data
    if raw_data is None:
        return Response("Bad Request", status=400)

    try:
        json_data = raw_data.decode("utf-8")
        # remove whitespaces and line breaks
        json_data = json.dumps(json.loads(json_data)).strip()
        result = compute_hmac_signature(json_data)
        return Response(
            json.dumps({"signature": result}), status=200, mimetype="application/json"
        )

    except Exception as e:
        return Response(str(e), status=500)


@app.route("/verify", methods=["POST"])
def _verify():
    data = request.json
    if data is None:
        return Response("Bad Request", status=400)
    try:
        signature = data.get("signature")
        payload = data.get("data")
        if (
            signature
            and payload
            and isinstance(signature, str)
            and isinstance(payload, dict)
        ):
            is_verified = verify_signature(
                signature=signature, payload=json.dumps(payload)
            )
            if is_verified:
                return Response("Signature Verified", status=204)
        return Response("Signature Verification Failed", status=400)
    except Exception as e:
        return Response(str(e), status=500)
