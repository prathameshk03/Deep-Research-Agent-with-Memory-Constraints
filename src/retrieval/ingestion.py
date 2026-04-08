import os
import uuid

class IngestionPipeline:
    def __init__(self, embedder, vector_db):
        self.embedder = embedder
        self.vector_db = vector_db

    def load_documents(self, folder_path: str) -> list[str]:
        docs = []

        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                    docs.append(f.read())

        return docs

    def chunk_text(self, text: str, chunk_size=100, overlap=20):
        chunks = []
        words = text.split()

        for i in range(0, len(words), chunk_size - overlap):
            chunk = words[i:i + chunk_size]
            chunks.append(" ".join(chunk))

        return chunks

    def process(self, folder_path: str):
        documents = self.load_documents(folder_path)

        all_chunks = []

        for doc in documents:
            chunks = self.chunk_text(doc)

            for chunk in chunks:
                embedding = self.embedder.embed(chunk)

                all_chunks.append({
                    "id": str(uuid.uuid4()),
                    "text": chunk,
                    "embedding": embedding
                })

        self.vector_db.add_documents(all_chunks)

        print(f"Ingested {len(all_chunks)} chunks into vector DB")