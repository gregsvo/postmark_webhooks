# postmark_webhooks
Flask app for incoming Postmark Webhooks

## Demo

The `demo/` folder contains a minimal Flask app (`main.py`) that receives a
Postmark bounce webhook, checks HTTP Basic Auth, and logs the bounce details.

### Setup

```
cd demo
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `WEBHOOK_USER` / `WEBHOOK_PASS` to the credentials you
want the webhook to require. `.env` is gitignored, so it stays local.

### Run

```
.venv/bin/python main.py
```

The server listens on `http://127.0.0.1:5000` (override with `PORT` in
`.env`).

### Test it

Test it in the Postmark Webhook creation dashboard, or by running the test_webhook.sh script:

`./demo/test_webhook.sh`
