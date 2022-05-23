import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import requests
from utils import hex_checker
from exceptions import APIError

load_dotenv()

app = Flask(__name__)

PROJECT_ID = os.environ.get("PROJECT_ID")
API_URL = f"https://mainnet.infura.io/v3/{PROJECT_ID}"


@app.errorhandler(APIError)
def handle_api_error(error: APIError):
    response = jsonify(error.to_dict())

    response.status_code = error.status_code

    return response


@app.route("/getLatestBlockNumber", methods=["GET"])
def eth_get_latest_block_by_number():
    api_obj = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}

    data = requests.post(API_URL, json=api_obj)

    return jsonify({"status": {"code": 200, "message": "Success"}, "data": data.json()})


@app.route("/getBlockByNumber", methods=["POST"])
def eth_get_block_by_number():
    data = request.json

    try:
        block_number = str(data["blockNumber"])
    except KeyError:
        return jsonify({"status": {"code": 400, "message": "Bad Request"}})

    if "showFullTransaction" in data:
        show_full_transaction = data["showFullTransaction"]
    else:
        show_full_transaction = False

    hex_checker(block_number, "Block Number")

    api_obj = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [block_number, show_full_transaction],
        "id": 1,
    }

    data = requests.post(API_URL, json=api_obj)

    return jsonify({"status": {"code": 200, "message": "Success"}, "data": data.json()})


@app.route("/getTransactionByBlockNumberAndIndex", methods=["POST"])
def eth_get_transaction_by_block_number_and_index():
    data = request.json

    try:
        block_number = str(data["blockNumber"])
        index = str(data["index"])
    except KeyError:
        return jsonify({"status": {"code": 400, "message": "Bad Request"}})

    hex_checker(block_number, "Block Number")
    hex_checker(index, "Index")

    api_obj = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionByBlockNumberAndIndex",
        "params": [block_number, index],
        "id": 1,
    }

    data = requests.post(API_URL, json=api_obj)

    return jsonify({"status": {"code": 200, "message": "Success"}, "data": data.json()})


if __name__ == "__main__":
    app.run(debug=True)
