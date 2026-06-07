import json

from agents.generator import generate_answer
from agents.factual_critic import check_facts
from agents.logic_critic import check_logic
from agents.completeness_critic import check_completeness
from agents.arbitrator import arbitrate


def run_workflow(question):
    answer = generate_answer(question)

    critiques = [
        check_facts(answer),
        check_logic(answer),
        check_completeness(answer)
    ]

    final_result = arbitrate(critiques)

    return {
        "question": question,
        "answer": answer,
        "final_result": final_result
    }


if __name__ == "__main__":
    question = "What is the capital of Canada?"
    result = run_workflow(question)

    with open("memory.json", "r") as f:
        memory = json.load(f)

    memory.append({
        "question": question,
        "answer": result["answer"],
        "verdict": result["final_result"]["verdict"],
        "score": result["final_result"]["average_score"]
    })

    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

    print(result)
