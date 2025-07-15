from langgraph.types import Send
from classes.State import State

def orchestrator(state: State):
    """Orchestrator that generates a plan for the report"""
    return {}

def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    return [Send("worker", {"section": section}) for section in state["sections"]]