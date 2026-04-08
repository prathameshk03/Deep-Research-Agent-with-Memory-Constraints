class ConstraintManager:
    def __init__(self, max_tokens, max_chunks, token_counter):
        self.max_tokens = max_tokens
        self.max_chunks = max_chunks
        self.token_counter = token_counter

    def limit_chunks(self, chunks: list[dict]) -> list[dict]:
        return chunks[:self.max_chunks]

    def enforce_token_limit(self, chunks, current_tokens):
        new_chunks = []
        
        for chunk in chunks:
            tokens = self.token_counter.count(chunk["text"])

            if current_tokens + tokens > self.max_tokens:
                break

            new_chunks.append(chunk)
            current_tokens += tokens

        return new_chunks, current_tokens