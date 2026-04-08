from retrieval.ingestion import IngestionPipeline
from retrieval.vector_store import VectorDB
from retrieval.embedder import Embedder
from core.system_builder import build_system


def ingest():
    embedder = Embedder()
    vector_db = VectorDB()

    pipeline = IngestionPipeline(embedder, vector_db)
    pipeline.process("data/sample_docs")


def main():
    ingest()  

    query = input("Enter your query: ")

    orchestrator = build_system()

    result = orchestrator.run(query)

    print("\n=== FINAL ANSWER ===\n")
    print(result["answer"])

    print("\n=== METRICS ===\n")
    print(result["metrics"])


if __name__ == "__main__":
    main()