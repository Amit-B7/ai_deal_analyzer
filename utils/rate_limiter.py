import time
import threading


class RateLimiter:
    def __init__(self, min_interval=3):
        self.min_interval = min_interval
        self.last_request = 0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request

            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)

            self.last_request = time.time()


rate_limiter = RateLimiter(min_interval=3)