from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm
from gen_tech_spec.classes.State import State
from gen_tech_spec.prompts.prompt import REFINE_REQUIREMENTS_SYSTEM_PROMPT, REFINE_REQUIREMENTS_HUMAN_PROMPT


def refine_requirements(state : State):
    """Generate refined requirements for the given topic"""

    # refiner = llm.with_structured_output(Requirements)

    requirements = llm.invoke([
        SystemMessage(content=REFINE_REQUIREMENTS_SYSTEM_PROMPT),
        HumanMessage(content=REFINE_REQUIREMENTS_HUMAN_PROMPT.format(user_input=state['topic']))
    ])

    return {"requirements" : requirements.content}
