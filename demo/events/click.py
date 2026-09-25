def handle_click(data):
    """Handle a Postmark Click event."""
    print(f"  Recipient: {data.get('Recipient')}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  Original Link: {data.get('OriginalLink')}")
    print(f"  Click Location: {data.get('ClickLocation')}")
    print(f"  Received At: {data.get('ReceivedAt')}")
    print()

    return "", 200
