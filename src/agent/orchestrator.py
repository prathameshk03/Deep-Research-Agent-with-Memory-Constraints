from config import MAX_CHUNKS_PER_QUERY, MAX_TOTAL_CHUNKS

class Orchestrator:
    def __init__(self, decomposer, retriever, memory_manager, constraint_manager, synthesizer, logger):
        self.decomposer = decomposer
        self.retriever = retriever
        self.memory_manager = memory_manager
        self.constraint_manager = constraint_manager
        self.synthesizer = synthesizer
        self.logger = logger

    def run(self, query: str) -> dict:
        self.logger.log("Starting query processing")

        sub_questions = self.decomposer.decompose(query)

        print(f"\n[LOG] Sub-questions: {sub_questions}\n")  # Debugging output to verify sub-questions

        all_context = []
        total_tokens = 0

        for sub_q in sub_questions:
            chunks = self.retriever.retrieve(sub_q)

            print(f"[LOG] Retrieved {len(chunks)} chunks for: {sub_q}")

            # Limit chunks per sub-question using ConstraintManager
            chunks = self.constraint_manager.limit_chunks_per_query(chunks)
            chunks = self.memory_manager.process(chunks)

            # Enforce token limit using ConstraintManager
            chunks, total_tokens = self.constraint_manager.enforce_token_limit(chunks, total_tokens)

            # Update logger with token and chunk usage
            self.logger.update_tokens(total_tokens)
            self.logger.update_chunks(len(chunks))

            all_context.extend(chunks)

        print(f"\n[LOG] Total context chunks used: {len(all_context)}\n")

        # Enforce global chunk limit using ConstraintManager
        all_context = self.constraint_manager.enforce_total_chunk_limit(all_context)

        self.logger.metrics["chunks_used"] = len(all_context)

        print(f"[LOG] Context after global limit: {len(all_context)}\n")

        # Generate the final answer
        final_answer = self.synthesizer.generate(query, all_context)

        # Retrieve metrics
        metrics = self.logger.get_metrics()

        return {
            "answer": final_answer,
            "metrics": metrics
        }