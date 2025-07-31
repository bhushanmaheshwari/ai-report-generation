from langchain_core.messages import SystemMessage, HumanMessage

from llm import llm
from gen_report.classes.State import State, WorkerState
from gen_report.prompts.prompt import PLANNER_SYSTEM_PROMPT, planner_human_prompt
from gen_report.classes.Sections import Sections

def planner(state: State):
    """Planner that generates a plan for the report"""

    planner = llm.with_structured_output(Sections)
    
    topic = f"{state['topic']}\n\nThis is an additional human input - {state.get('human_message', '')}"

    report_sections = planner.invoke([
        SystemMessage(content=PLANNER_SYSTEM_PROMPT),
        HumanMessage(content=planner_human_prompt(topic))
    ])
    return {"sections": report_sections.sections}
