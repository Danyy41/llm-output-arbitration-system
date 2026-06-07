from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents.generator import generate_answer
from agents.factual_critic import check_facts


class WorkflowState(TypedDict):
    question: str
    answer: str
    factual_critique: dict


def generator_node(state):
    answer = generate_answer(state["question"])
    return {
        "answer": answer
    }


def factual_critic_node(state):
    critique = check_facts(state["answer"])
    return {
        "factual_critique": critique
    }


graph = StateGraph(WorkflowState)

graph.add_node("generator", generator_node)
graph.add_node("factual_critic", factual_critic_node)

graph.add_edge(START, "generator")
graph.add_edge("generator", "factual_critic")
graph.add_edge("factual_critic", END)

app = graph.compile()

result = app.invoke({
    "question": "What is the capital of Canada?"
})

print(result)
