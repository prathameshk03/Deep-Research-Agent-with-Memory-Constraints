from src.agent.orchestrator import Orchestrator
from src.agent.decomposer import Decomposer
from src.agent.synthesizer import Synthesizer
from src.memory.memory_manager import MemoryManager
from src.memory.summarizer import Summarizer
from src.retrieval.vector_store import VectorDB
from src.retrieval.embedder import Embedder
from src.retrieval.retriever import Retriever
from src.constraints.constraint_manager import ConstraintManager
from src.utils.logger import Logger
from src.utils.token_counter import TokenCounter
from src.utils.llm_client import LLMClient

def build_system():
    llm = LLMClient()
    embedder = Embedder()
    vector_db = VectorDB()

    decomposer = Decomposer(llm)
    retriever = Retriever(vector_db, embedder)
    summarizer = Summarizer(llm)
    memory_manager = MemoryManager(summarizer)
    constraint_manager = ConstraintManager(
        max_tokens=2000,
        max_chunks=5,
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