from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm
from classes.State import WorkerState
from prompt import WORKER_SYSTEM_PROMPT, worker_human_prompt

def worker(state: WorkerState):
    """Worker writes a section of the report"""

    section = llm.invoke(
        [
            SystemMessage(
                content=WORKER_SYSTEM_PROMPT
            ),
            HumanMessage(
                content=worker_human_prompt(state['section'].name, state['section'].description)
            )
        ]
    )

    return {
        "section_summaries": [f"{state['section'].name} | {state['section'].description}"],
        "completed_sections": [section.content]
    }