class Synthesizer:
    def __init__(self, llm_client):
        self.llm = llm_client

    def generate(self, query: str, context: list[dict]) -> str:
        context_text = "\n\n".join([c["text"] for c in context])

        prompt = f"""
        You MUST answer ONLY using the provided context.
        Do NOT use prior knowledge.

        If the context is insufficient, explicitly say:
        "Insufficient information in provided context."

        Query:
        {query}

        Context:
        {context_text}

        Provide a structured answer.
        """

        return self.llm.generate(prompt)