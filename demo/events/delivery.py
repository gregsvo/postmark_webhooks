def handle_delivery(data):
    """Handle a Postmark Delivery event."""
    print(f"  Recipient: {data.get('Recipient')}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  Delivery Message: {data.get('DeliveryMessage')}")
    print(f"  Delivered At: {data.get('DeliveredAt')}")
    print()

    return "", 200
