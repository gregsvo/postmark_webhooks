def handle_subscription_change(data):
    """Handle a Postmark SubscriptionChange event."""
    print(f"  Recipient: {data.get('Recipient')}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  Action Type: {data.get('ActionType')}")
    print(f"  Suppress Sending: {data.get('SuppressSending')}")
    print(f"  Suppression Reason: {data.get('SuppressionReason')}")
    print()

    return "", 200
