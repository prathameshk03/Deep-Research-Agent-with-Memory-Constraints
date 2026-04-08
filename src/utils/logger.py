import time

class Logger:
    def __init__(self):
        self.metrics = {
            "start_time": time.time(),
            "tokens_used": 0,
            "chunks_used": 0,
        }

    def log(self, message: str):
        print(f"[LOG] {message}")

    def update_tokens(self, tokens: int):
        self.metrics["tokens_used"] += tokens

    def update_chunks(self, count: int):
        self.metrics["chunks_used"] += count

    def get_metrics(self):
        self.metrics["latency"] = time.time() - self.metrics["start_time"]
        return self.metrics