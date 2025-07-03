from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.types import Send

from gen_report.tools.llm import planner
from gen_report.classes.State import State, WorkerState
from gen_report.prompts.prompt import ORCHESTRATOR_SYSTEM_PROMPT, orchestrator_human_prompt
from gen_report.classes.Sections import Sections

def orchestrator(state: State):
    """Orchestrator that generates a plan for the report"""

    planner = llm.with_structured_output(Sections)
    # Generate queries
    report_sections = planner.invoke([
        SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT),
        HumanMessage(content=orchestrator_human_prompt(state['topic']))
    ])

    return {"sections": report_sections.sections}


def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    return [Send("worker", {"section": section}) for section in state["sections"]]