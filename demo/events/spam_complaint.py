def handle_spam_complaint(data):
    """Handle a Postmark SpamComplaint event."""
    print(f"  Email: {data.get('Email')}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  Description: {data.get('Description')}")
    print(f"  Details: {data.get('Details')}")
    print()

    return "", 200
