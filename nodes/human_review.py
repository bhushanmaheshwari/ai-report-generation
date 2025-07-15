from langchain_core.messages import SystemMessage, HumanMessage
from classes.State import State
from classes.Sections import HumanApproval
from langgraph.types import interrupt, Command
from prompt import HUMAN_REVIEW_SYSTEM_PROMPT, human_review_human_prompt
from llm import llm

def human_review(state: State):
    """Human review node that waits for approval"""

    user_added_inputs = interrupt(state['sections'])

    # If human input is present, process it
    approval_llm = llm.with_structured_output(HumanApproval)
    human_approved = approval_llm.invoke([
        SystemMessage(content=HUMAN_REVIEW_SYSTEM_PROMPT),
        HumanMessage(content=human_review_human_prompt(state['sections'], user_added_inputs))
    ])

    return {"human_approved": human_approved.approved, "human_message": user_added_inputs}

def human_decision(state):
    if state.get("human_approved"):
        return "orchestrator"
    else:
        return "planner"