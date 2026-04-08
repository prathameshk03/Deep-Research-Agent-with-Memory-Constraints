import chromadb
from chromadb.config import Settings

class VectorDB:
    def __init__(self, collection_name="documents"):
        self.client = chromadb.Client(
            Settings(persist_directory="chroma_db")
        )
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_documents(self, docs: list[dict]):
        """
        docs = [
            {
                "id": str,
                "text": str,
                "embedding": list[float]
            }
        ]
        """
        self.collection.add(
            ids=[doc["id"] for doc in docs],
            documents=[doc["text"] for doc in docs],
            embeddings=[doc["embedding"] for doc in docs]
        )

    def similarity_search(self, embedding, top_k=5):
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        print(f"[LOG] DB contains {self.collection.count()} documents")

        # Normalize output
        output = []
        for i in range(len(results["documents"][0])):
            output.append({
                "text": results["documents"][0][i],
                "score": results["distances"][0][i]
            })

        return output