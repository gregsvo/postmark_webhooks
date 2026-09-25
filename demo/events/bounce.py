def handle_bounce(data):
    """Handle a Postmark Bounce event."""
    bounce_type = data.get("Type")

    print(f"  Email: {data.get('Email')}")
    print(f"  Type: {bounce_type}")
    print(f"  Message ID: {data.get('MessageID')}")
    print(f"  Description: {data.get('Description')}")
    print(f"  Details: {data.get('Details')}")

    # Decide what to do with the bounce
    action = (
        "Remove from mailing list"
        if bounce_type == "HardBounce"
        else "Retry later"
    )

    print(f"  Action: {action}")
    print()

    return "", 200
