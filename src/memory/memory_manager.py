class MemoryManager:
    def __init__(self, summarizer):
        self.summarizer = summarizer

    def process(self, chunks: list[dict]) -> list[dict]:
        chunks = self._deduplicate(chunks)
        chunks = self._rank(chunks)
        return chunks

    def summarize(self, chunks: list[dict]) -> list[dict]:
        combined_text = "\n".join([c["text"] for c in chunks])

        summary = self.summarizer.summarize(combined_text)

        return [{"text": summary, "source": "summary"}]

    def _deduplicate(self, chunks):
        seen = set()
        unique = []

        for c in chunks:
            if c["text"] not in seen:
                seen.add(c["text"])
                unique.append(c)

        return unique

    def _rank(self, chunks):
        return sorted(chunks, key=lambda x: x["score"], reverse=True)