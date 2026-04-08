class Decomposer:
    def __init__(self, llm_client):
        self.llm = llm_client

    def decompose(self, query: str) -> list[str]:
        prompt = f"""
        Break the following query into 3-5 clear, non-overlapping sub-questions.

        Query: {query}

        Return ONLY a numbered list.
        """

        response = self.llm.generate(prompt)

        return self._parse_response(response)

    def _parse_response(self, response: str) -> list[str]:
        lines = response.split("\n")
        cleaned = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # remove numbering like "1. "
            if "." in line:
                line = line.split(".", 1)[-1].strip()

            cleaned.append(line)

        return cleaned[:5]