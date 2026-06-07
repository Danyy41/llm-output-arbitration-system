from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class WorkflowState(TypedDict):
    question: str
    answer: str


def generator_node(state):
    return {
        "answer": f"Generated answer for: {state['question']}"
    }


graph = StateGraph(WorkflowState)

graph.add_node("generator", generator_node)

graph.add_edge(START, "generator")
graph.add_edge("generator", END)

app = graph.compile()

result = app.invoke({
    "question": "What is the capital of Canada?"
})

print(result)
