class TokenCounter:
    def count(self, text: str) -> int:
        """
        Approximate token count using word count.
        """
        return len(text.split())