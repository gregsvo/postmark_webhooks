import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

app = Flask(__name__)

WEBHOOK_USER = os.environ["WEBHOOK_USER"]
WEBHOOK_PASS = os.environ["WEBHOOK_PASS"]


@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle a Postmark webhook."""
    # Verify HTTP Basic Auth
    auth = request.authorization
    if not auth or (
        auth.username != WEBHOOK_USER
        or auth.password != WEBHOOK_PASS
    ):
        print("Authentication failed")
        return jsonify({"error": "Unauthorized"}), 401

    print(f"Authenticated as: {auth.username}")

    # Read the webhook payload
    data = request.get_json()

    print(f"\nWebhook payload: {data}")


    # Extract the fields we care about
    email = data.get("Email")
    bounce_type = data.get("Type")
    message_id = data.get("MessageID")
    description = data.get("Description")
    details = data.get("Details")

    print("\nBounce received:")
    print(f"  Email: {email}")
    print(f"  Type: {bounce_type}")
    print(f"  Message ID: {message_id}")
    print(f"  Description: {description}")
    print(f"  Details: {details}")

    # Decide what to do with the bounce
    action = (
        "Remove from mailing list"
        if bounce_type == "HardBounce"
        else "Retry later"
    )

    print(f"Action: {action}\n")

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)