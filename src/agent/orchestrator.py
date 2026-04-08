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

        all_context = []
        total_tokens = 0

        for sub_q in sub_questions:
            chunks = self.retriever.retrieve(sub_q)

            chunks = self.constraint_manager.limit_chunks(chunks)

            chunks = self.memory_manager.process(chunks)

            chunks, total_tokens = self.constraint_manager.enforce_token_limit(
                chunks, total_tokens
            )

            all_context.extend(chunks)

        final_answer = self.synthesizer.generate(query, all_context)

        metrics = self.logger.get_metrics()

        return {
            "answer": final_answer,
            "metrics": metrics
        }