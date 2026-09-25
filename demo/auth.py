import os
from functools import wraps

from flask import jsonify, request

WEBHOOK_USER = os.environ["WEBHOOK_USER"]
WEBHOOK_PASS = os.environ["WEBHOOK_PASS"]
REQUIRE_AUTH = os.environ.get("REQUIRE_AUTH", "True").lower() == "true"

def require_basic_auth(view):
    @wraps(view)
    def wrapper():
        if not REQUIRE_AUTH:
            return view()

        auth = request.authorization
        if not auth or auth.username != WEBHOOK_USER or auth.password != WEBHOOK_PASS:
            print("Authentication failed")
            return jsonify({"error": "Unauthorized"}), 401

        return view()

    return wrapper
