import threading
from collections import OrderedDict

# Caps memory use for long-running processes; old entries are evicted once
# retries are extremely unlikely to still be in flight.
MAX_TRACKED_EVENTS = 10000

_lock = threading.Lock()
_seen_trace_ids = OrderedDict()


def is_duplicate(trace_id):
    """Check whether this X-PM-Webhook-Trace-Id has already been processed, recording it if not.

    The trace ID identifies a single event delivery (and stays stable across that
    event's own retries), unlike MessageID which is shared by every event type
    (Delivery, Open, Click, Bounce, ...) raised for the same email.

    Returns True if the event was already seen (a retried or timed-out-but-successful
    delivery), so the caller can skip re-running side effects.
    """
    if not trace_id:
        return False

    with _lock:
        if trace_id in _seen_trace_ids:
            return True

        _seen_trace_ids[trace_id] = True
        if len(_seen_trace_ids) > MAX_TRACKED_EVENTS:
            _seen_trace_ids.popitem(last=False)

        return False
