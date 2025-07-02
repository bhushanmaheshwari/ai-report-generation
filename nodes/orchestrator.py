from langchain_core.messages import SystemMessage, HumanMessage
from llm import planner
from classes.State import State, WorkerState
from langgraph.types import Send
from prompt import ORCHESTRATOR_SYSTEM_PROMPT, orchestrator_human_prompt

def orchestrator(state: State):
    """Orchestrator that generates a plan for the report"""

    # Generate queries
    report_sections = planner.invoke([
        SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT),
        HumanMessage(content=orchestrator_human_prompt(state['topic']))
    ])

    return {"sections": report_sections.sections}


def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    return [Send("worker", {"section": section}) for section in state["sections"]]