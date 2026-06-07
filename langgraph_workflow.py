from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class WorkflowState(TypedDict):
    question: str
    answer: str


from agents.generator import generate_answer

def generator_node(state):
    answer = generate_answer(state["question"])
    return {
        "answer": answer
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
