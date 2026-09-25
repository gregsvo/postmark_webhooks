import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

from auth import require_basic_auth
from dedupe import is_duplicate
from events.bounce import handle_bounce
from events.click import handle_click
from events.delivery import handle_delivery
from events.open import handle_open
from events.spam_complaint import handle_spam_complaint
from events.subscription_change import handle_subscription_change

logging.getLogger("werkzeug").setLevel(logging.ERROR)


app = Flask(__name__)

HANDLERS = {
    "Bounce": handle_bounce,
    "Open": handle_open,
    "Click": handle_click,
    "SubscriptionChange": handle_subscription_change,
    "SpamComplaint": handle_spam_complaint,
    "Delivery": handle_delivery,
}


@app.route("/", methods=["POST"])
@require_basic_auth
def events():
    trace_id = request.headers.get("X-PM-Webhook-Trace-Id")
    if is_duplicate(trace_id):
        print(f"  Duplicate delivery, already processed (Trace ID: {trace_id})\n")
        return "", 200

    data = request.get_json()
    record_type = data.get("RecordType")
    handler = HANDLERS.get(record_type)

    if handler is None:
        print(f"  Unhandled RecordType: {record_type}\n")
        return jsonify({"error": f"Unsupported RecordType: {record_type}"}), 400

    return handler(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on port {port}")
    app.run(port=port, debug=True)
