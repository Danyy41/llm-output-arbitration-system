from typing import TypedDict
from langgraph.graph import StateGraph


class WorkflowState(TypedDict):
    question: str


graph = StateGraph(WorkflowState)

print("LangGraph is working")
