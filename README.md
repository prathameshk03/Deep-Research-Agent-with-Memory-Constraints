# Deep Research Agent with Memory Constraints

## Overview

This project implements a **constraint-aware research agent** that answers complex queries by combining:

* Query decomposition
* Retrieval-Augmented Generation (RAG)
* Memory and token constraint enforcement

Unlike a standard chatbot, this system is designed to operate under **strict context and token limits**, mimicking real-world production constraints.

---

## Key Features

* **Multi-step Query Decomposition**
  Breaks complex queries into smaller, focused sub-questions

* **Retrieval-Augmented Generation (RAG)**
  Uses a vector database (Chroma) to retrieve relevant context

* **Constraint-Aware Processing**
  Enforces:

  * Per-sub-question chunk limits
  * Global context limits
  * Token usage limits

* **Persistent Memory (Vector DB)**
  Stores and retrieves knowledge efficiently across runs

* **Structured Output Generation**
  Produces clear, organized answers grounded in retrieved data

---

## Architecture

```text
User Query
 → Decomposer (LLM)
 → Retriever (Vector DB)
 → Memory Manager
 → Constraint Manager
 → Synthesizer (LLM)
 → Final Answer
```

---

## Tech Stack

* **LLM**: Groq (LLaMA 3.1)
* **Embeddings**: sentence-transformers
* **Vector Database**: ChromaDB
* **Language**: Python

---

## Project Structure

```text
src/
├── agent/           # Orchestrator, decomposer, synthesizer
├── retrieval/       # Vector DB, embedder, ingestion
├── memory/          # Memory manager, summarizer
├── constraints/     # Constraint logic
├── utils/           # Logger, token counter, LLM client
├── core/            # System builder
└── main.py          # Entry point

data/
└── sample_docs/     # Input documents
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/prathameshk03/Deep-Research-Agent-with-Memory-Constraints.git
cd Deep-Research-Agent-with-Memory-Constraints
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
MAX_TOKENS=2000
MAX_CHUNKS_PER_QUERY=3
MAX_TOTAL_CHUNKS=8
```

---

## Usage

### 1. Ingest documents

```bash
python src/main.py
```

(Initial ingestion runs automatically)

---

### 2. Run the agent

```bash
python src/main.py
```

Example query:

```text
Compare AWS vs GCP autoscaling cost and performance
```

---

## Example Queries

You can test the agent with complex, multi-part queries such as:

* Compare AWS vs GCP autoscaling cost and performance
* How do Kubernetes autoscaling mechanisms (HPA vs VPA) impact cost and resource utilization?
* Compare autoscaling strategies across AWS, GCP, and Kubernetes in terms of scalability and cost

These queries demonstrate the agent’s ability to:

* Decompose complex questions
* Retrieve relevant context
* Generate structured, grounded responses

---

## Example Output

* Structured comparison (cost, performance, tradeoffs)
* Context-aware responses grounded in retrieved data
* Metrics including token usage and chunk count

---

## Configuration

The system supports configurable constraints via environment variables. These values are loaded via a centralized config module (`config.py`) and used across the system.

```env
GROQ_API_KEY=your_api_key_here
MAX_TOKENS=2000
MAX_CHUNKS_PER_QUERY=3
MAX_TOTAL_CHUNKS=8
```

### Parameter Details

* **MAX_TOKENS**
  Maximum token budget per query. Controls how much total context is passed to the LLM.

* **MAX_CHUNKS_PER_QUERY**
  Number of chunks retrieved per sub-question. Helps reduce noise and improve relevance.

* **MAX_TOTAL_CHUNKS**
  Maximum number of chunks passed to the LLM after aggregation. Enforces global memory constraints.

### Tuning Trade-offs

* Higher values → better accuracy, higher cost and latency
* Lower values → faster and cheaper, but less detailed responses

These parameters allow flexible tuning of **accuracy vs cost vs latency**.

---

## Constraints Implemented

* **Per-sub-question chunk limit** (e.g., 3 chunks)
* **Global context limit** (e.g., 8 chunks total)
* **Token budget enforcement** (e.g., 2000 tokens max)

---

## Metrics Tracked

* Tokens used
* Number of context chunks
* Latency

---

## Evaluation

See `evaluation.md` for:

* Architecture decisions
* Memory strategy
* Tradeoffs
* Failure cases
* Future improvements

---

## Future Improvements

* Tokenization aligned with model (tiktoken)
* Retrieval re-ranking
* Caching for repeated queries
* Improved summarization for large contexts

---
