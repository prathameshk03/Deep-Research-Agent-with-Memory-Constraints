from config import MAX_TOKENS, MAX_CHUNKS_PER_QUERY, MAX_TOTAL_CHUNKS

from agent.orchestrator import Orchestrator
from agent.decomposer import Decomposer
from agent.synthesizer import Synthesizer
from memory.memory_manager import MemoryManager
from memory.summarizer import Summarizer
from retrieval.vector_store import VectorDB
from retrieval.embedder import Embedder
from retrieval.retriever import Retriever
from constraints.constraint_manager import ConstraintManager
from utils.logger import Logger
from utils.token_counter import TokenCounter
from utils.llm_client import LLMClient

def build_system():
    # Load constraints from environment variables
    max_tokens = MAX_TOKENS
    max_chunks_per_query = MAX_CHUNKS_PER_QUERY
    max_total_chunks = MAX_TOTAL_CHUNKS

    llm = LLMClient()
    embedder = Embedder()
    vector_db = VectorDB()

    decomposer = Decomposer(llm)
    retriever = Retriever(vector_db, embedder)
    summarizer = Summarizer(llm)
    memory_manager = MemoryManager(summarizer)

    constraint_manager = ConstraintManager(
        max_tokens=max_tokens,
        max_chunks_per_query=max_chunks_per_query,
        max_total_chunks=max_total_chunks,
        token_counter=TokenCounter()
    )

    synthesizer = Synthesizer(llm)
    logger = Logger()

    return Orchestrator(
        decomposer,
        retriever,
        memory_manager,
        constraint_manager,
        synthesizer,
        logger
    )