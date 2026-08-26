#!/usr/bin/env bash
set -euo pipefail

# Loads WEBHOOK_USER / WEBHOOK_PASS from .env so credentials stay in sync with the running server.
cd "$(dirname "$0")"
set -a
source .env
set +a

URL="${1:-$NGROK_ENDPOINT}"

curl -i -u "${WEBHOOK_USER}:${WEBHOOK_PASS}" -X POST "$URL" \
  -H "Content-Type: application/json" \
  -d '{
        "ID": 42,
        "Type": "HardBounce",
        "RecordType": "Bounce",
        "TypeCode": 1,
        "Tag": "Test",
        "MessageID": "00000000-0000-0000-0000-000000000000",
        "Details": "Test bounce details",
        "Email": "john@example.com",
        "From": "sender@example.com",
        "BouncedAt": "2026-08-25T13:36:42Z",
        "Inactive": true,
        "DumpAvailable": true,
        "CanActivate": true,
        "Subject": "Test subject",
        "ServerID": 1234,
        "MessageStream": "outbound",
        "Content": "Test content",
        "Name": "Hard bounce",
        "Description": "The server was unable to deliver your message (ex: unknown user, mailbox not found).",
        "Metadata": {
          "example": "value",
          "example_2": "value"
        }
  }'
