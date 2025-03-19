from flask import Flask, Response, request

from business_logic.decryption import decrypt_json_depth_1
from business_logic.encryption import encrypt_json_depth_1

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


@app.route("/sign")
def _sign():
    return "to be implemented"


@app.route("/verify")
def _verify():
    return "to be implemented"
