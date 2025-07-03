from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm
from gen_tech_spec.classes.State import State
from gen_tech_spec.prompts.prompt import TECH_STACK_SYSTEM_PROMPT, TECH_STACK_HUMAN_PROMPT


def generate_tech_stack(state : State):
    """Enlist technology stack based on the given requirements"""

    components = llm.invoke([
        SystemMessage(content=TECH_STACK_SYSTEM_PROMPT),
        HumanMessage(content=TECH_STACK_HUMAN_PROMPT.format(refined_requirements=state['requirements']))
    ])

    return {"components" : components.content}

