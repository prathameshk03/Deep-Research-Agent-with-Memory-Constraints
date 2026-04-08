class Summarizer:
    def __init__(self, llm_client):
        self.llm = llm_client

    def summarize(self, text: str) -> str:
        prompt = f"""
        Summarize the following content while preserving key technical details:

        {text}

        Keep it concise but informative.
        """

        return self.llm.generate(prompt)