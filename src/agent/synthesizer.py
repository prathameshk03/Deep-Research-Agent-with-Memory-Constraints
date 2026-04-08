class Synthesizer:
    def __init__(self, llm_client):
        self.llm = llm_client

    def generate(self, query: str, context: list[dict]) -> str:
        context_text = "\n".join([c["text"] for c in context])

        prompt = f"""
        You are a research assistant.

        Answer the query using the context below.

        Query: {query}

        Context:
        {context_text}

        Provide a structured and concise answer.
        """

        return self.llm.generate(prompt)