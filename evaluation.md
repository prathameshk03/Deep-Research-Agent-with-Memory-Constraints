# Deep Research Agent with Memory Constraints – Evaluation

## 1. Problem Understanding

The goal of this project was to design a research agent capable of answering complex, multi-part queries under strict memory and token constraints. Unlike a simple LLM-based chatbot, the system must:

* Decompose complex queries into smaller sub-questions
* Retrieve only relevant context from a knowledge base
* Operate within defined token and memory limits
* Synthesize a final answer grounded in retrieved data

This requires balancing **accuracy, efficiency, and cost**, which is a core challenge in real-world LLM systems.

---

## 2. System Architecture

The system follows a modular, pipeline-based architecture:

```
User Query
 → Decomposer (LLM)
 → Retriever (Vector DB)
 → Memory Manager
 → Constraint Manager
 → Synthesizer (LLM)
 → Final Answer
```

### Key Components

* **Decomposer**: Breaks complex queries into 3–5 focused sub-questions
* **Retriever (RAG)**: Uses embeddings + ChromaDB to fetch relevant chunks
* **Memory Manager**: Deduplicates, ranks, and prepares context
* **Constraint Manager**: Enforces token and chunk limits
* **Synthesizer**: Generates final structured response using retrieved context

This separation of concerns makes the system **scalable, testable, and extensible**.

---

## 3. Memory & Retrieval Strategy

The system uses a **Retrieval-Augmented Generation (RAG)** approach:

* Documents are chunked and embedded using `sentence-transformers`
* Stored in a persistent Chroma vector database
* Retrieved using similarity search per sub-question

### Memory Design

The agent uses a hybrid memory strategy:

* **Short-term memory**: Context accumulated during a single query
* **Long-term memory**: Vector database (persistent knowledge base)

### Optimization Techniques

* Chunking with overlap for better semantic retrieval
* Deduplication and ranking of retrieved chunks
* Limiting chunks per sub-question to reduce noise

---

## 4. Constraint Design

A key focus of this system is **explicit constraint enforcement** to ensure bounded memory usage and predictable LLM behavior.

### Implemented Constraints

1. **Per-sub-question constraint**

   ```python
   chunks = chunks[:MAX_CHUNKS_PER_QUERY]
   ```

2. **Token constraint**

   ```python
   MAX_TOKENS = 2000
   ```

3. **Global context constraint**

   ```python
   all_context = all_context[:MAX_TOTAL_CHUNKS]
   ```

### Configurability

All constraint parameter values (e.g., `MAX_TOKENS`, `MAX_CHUNKS_PER_QUERY`, `MAX_TOTAL_CHUNKS`) are centralized in a dedicated `config.py` module, which loads environment variables and exposes them across the system.
This allows the system to be tuned without modifying code, enabling flexible trade-offs between accuracy, latency, and cost.

### Design Rationale

* **Per-sub-question limits** reduce noise early in the pipeline and improve retrieval precision
* **Token constraints** ensure the system operates within a bounded LLM context window
* **Global context limits** prevent uncontrolled memory growth across multiple sub-queries

This multi-level constraint design ensures that the system remains both **efficient and scalable**, while maintaining answer quality.


---

## 5. Observability & Metrics

The system tracks:

* Total tokens used
* Number of chunks used
* Latency

Example:

```json
{
  "tokens_used": 1315,
  "chunks_used": 8,
  "latency": 1.5
}
```

This allows evaluation of:

* Efficiency vs accuracy tradeoffs
* Impact of constraint tuning
* System performance under load

---

## 6. Key Design Decisions

### 1. RAG over full-context prompting

* More scalable
* Reduces token usage
* Improves relevance

---

### 2. Query decomposition

* Improves retrieval precision
* Handles complex queries effectively

---

### 3. Multi-level constraints

* Per-query + global constraints
* Ensures bounded context

---

### 4. Persistence in vector DB

* Ensures ingestion and retrieval consistency
* Avoids common issue of empty retrieval results

---

## 7. Tradeoffs

### Accuracy vs Token Usage

* More context → better answers but higher cost
* Less context → faster but risk of missing information

### Latency vs Completeness

* More sub-questions improve coverage
* But increase response time

### Simplicity vs Precision

* Approximate token counting is fast
* Exact tokenization would improve accuracy

---

## 8. Failure Cases

* **Insufficient data in vector DB** → incomplete answers
* **Poor chunking** → irrelevant retrieval
* **Ambiguous queries** → suboptimal decomposition
* **LLM hallucination risk** (mitigated via grounding prompt)

---

## 9. Improvements & Future Work

* Use model-aligned token counting (e.g., tiktoken)
* Add re-ranking of retrieved chunks
* Introduce caching for repeated queries
* Improve summarization for long contexts
* Add evaluation benchmarks (precision/recall of retrieval)

---

## 10. Conclusion

This system demonstrates a **constraint-aware research agent** that:

* Handles complex queries through decomposition
* Retrieves and filters relevant context efficiently
* Operates within strict memory and token limits
* Produces structured, grounded responses

The design reflects real-world considerations such as **cost control, scalability, and robustness**, which are critical for deploying LLM-powered systems in production environments.

---
