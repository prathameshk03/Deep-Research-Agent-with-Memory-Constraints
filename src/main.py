from core.system_builder import build_system 

def main():
    query = input("Enter your query: ")

    orchestrator = build_system()

    result = orchestrator.run(query)

    print("\n=== FINAL ANSWER ===\n")
    print(result["answer"])

    print("\n=== METRICS ===\n")
    print(result["metrics"])