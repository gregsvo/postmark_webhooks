def handle_open(data):
    """Handle a Postmark Open event."""
    print(f"  Recipient: {data.get('Recipient')}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  First Open: {data.get('FirstOpen')}")
    print(f"  Platform: {data.get('Platform')}")
    print(f"  Received At: {data.get('ReceivedAt')}")
    print()

    return "", 200
