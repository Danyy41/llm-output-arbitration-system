from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents.generator import generate_answer
from agents.factual_critic import check_facts
from agents.logic_critic import check_logic
from agents.completeness_critic import check_completeness
from agents.arbitrator import arbitrate


class WorkflowState(TypedDict):
    question: str
    answer: str
    factual_critique: dict
    logic_critique: dict
    completeness_critique: dict
    final_result: dict


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


def logic_critic_node(state):
    critique = check_logic(state["answer"])
    return {
        "logic_critique": critique
    }


def completeness_critic_node(state):
    critique = check_completeness(state["answer"])
    return {
        "completeness_critique": critique
    }


def arbitrator_node(state):
    critiques = [
        state["factual_critique"],
        state["logic_critique"],
        state["completeness_critique"]
    ]

    result = arbitrate(critiques)

    return {
        "final_result": result
    }


graph = StateGraph(WorkflowState)

graph.add_node("generator", generator_node)
graph.add_node("factual_critic", factual_critic_node)
graph.add_node("logic_critic", logic_critic_node)
graph.add_node("completeness_critic", completeness_critic_node)
graph.add_node("arbitrator", arbitrator_node)

graph.add_edge(START, "generator")
graph.add_edge("generator", "factual_critic")
graph.add_edge("factual_critic", "logic_critic")
graph.add_edge("logic_critic", "completeness_critic")
graph.add_edge("completeness_critic", "arbitrator")
graph.add_edge("arbitrator", END)

app = graph.compile()
graph_png = app.get_graph().draw_mermaid()

print(graph_png)
result = app.invoke({
    "question": "What is the capital of Canada?"
})

print(result)
