# token_manager.py

import time
import uuid

class TokenManager:
    """
    Handles session token generation, validation, and expiry checks using O(1) lookup.
    """

    def __init__(self):
        self.tokens = {}  # token: expiry_time

    def generate_token(self, expiry_seconds=3600):
        token = str(uuid.uuid4())
        expiry_time = int(time.time()) + expiry_seconds
        self.tokens[token] = expiry_time
        return token

    def validate_token(self, token):
        current_time = int(time.time())
        expiry_time = self.tokens.get(token)

        if expiry_time is None:
            return False  # Token doesn't exist

        if expiry_time < current_time:
            self.tokens.pop(token)  # Remove expired token
            return False

        return True  # Token valid (O(1) check)

    def invalidate_token(self, token):
        self.tokens.pop(token, None)  # O(1) removal
