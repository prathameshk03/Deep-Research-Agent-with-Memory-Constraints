class Retriever:
    def __init__(self, vector_db, embedder):
        self.vector_db = vector_db
        self.embedder = embedder

    def retrieve(self, query: str) -> list[dict]:
        embedding = self.embedder.embed(query)

        results = self.vector_db.similarity_search(
            embedding=embedding,
            top_k=5
        )

        return results