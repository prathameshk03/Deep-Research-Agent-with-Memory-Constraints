class Decomposer:
    def __init__(self, llm_client):
        self.llm = llm_client

    def decompose(self, query: str) -> list[str]:
        prompt = f"""
        Break the following query into 3-5 focused sub-questions:
        Query: {query}
        """

        response = self.llm.generate(prompt)

        return self._parse_response(response)

    def _parse_response(self, response: str) -> list[str]:
        # Convert numbered list → Python list
        lines = response.split("\n")
        return [line.strip() for line in lines if line.strip()]