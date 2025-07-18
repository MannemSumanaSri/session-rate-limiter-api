# rate_limiter.py

import time

class RateLimiter:
    """
    Simple rate limiter allowing max_requests per time_window_seconds.
    Tracks per-user request counts using O(1) dictionary lookup.
    """

    def __init__(self, max_requests=5, time_window_seconds=60):
        self.max_requests = max_requests
        self.time_window_seconds = time_window_seconds
        self.user_requests = {}  # token: (count, window_start_time)

    def is_allowed(self, token):
        current_time = int(time.time())
        count, window_start = self.user_requests.get(token, (0, current_time))

        if current_time - window_start >= self.time_window_seconds:
            # Reset the window
            count = 0
            window_start = current_time

        if count >= self.max_requests:
            # Rate limit exceeded
            self.user_requests[token] = (count, window_start)
            return False

        # Allow request
        self.user_requests[token] = (count + 1, window_start)
        return True
