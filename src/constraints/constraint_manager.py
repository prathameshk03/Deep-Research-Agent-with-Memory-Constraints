class ConstraintManager:
    def __init__(self, max_tokens, max_chunks_per_query, max_total_chunks, token_counter):
        self.max_tokens = max_tokens
        self.max_chunks_per_query = max_chunks_per_query
        self.max_total_chunks = max_total_chunks
        self.token_counter = token_counter

    def limit_chunks_per_query(self, chunks: list[dict]) -> list[dict]:
        """
        Limits the number of chunks per query to max_chunks_per_query.
        """
        return chunks[:self.max_chunks_per_query]

    def enforce_token_limit(self, chunks, current_tokens):
        """
        Enforces the token limit by iterating through chunks and ensuring
        the total token count does not exceed max_tokens.
        """
        new_chunks = []
        
        for chunk in chunks:
            tokens = self.token_counter.count(chunk["text"])

            if current_tokens + tokens > self.max_tokens:
                break

            new_chunks.append(chunk)
            current_tokens += tokens

        return new_chunks, current_tokens

    def enforce_total_chunk_limit(self, all_chunks: list[dict]) -> list[dict]:
        """
        Enforces the total chunk limit across all queries.
        """
        return all_chunks[:self.max_total_chunks]