# postmark_webhooks
Flask app for incoming Postmark Webhooks

## Demo

The `demo/` folder contains a minimal Flask app (`main.py`) with a single
`/` endpoint that checks HTTP Basic Auth, then dispatches each incoming
Postmark event (Bounce, Open, Click, SpamComplaint, Delivery,
SubscriptionChange) to its own handler in `events/` based on the payload's
`RecordType`.

### Setup

```
cd demo
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `WEBHOOK_USER` / `WEBHOOK_PASS` to the credentials you
want the webhook to require. (.env is git ignored)

### Run

```
.venv/bin/python main.py
```

The server listens on `http://127.0.0.1:5000` (override with `PORT` in
`.env`).

### Test it

Use the "Send test" option in the Postmark Webhook creation dashboard to send a
sample event to your running server.
