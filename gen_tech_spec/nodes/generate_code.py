from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm
from gen_tech_spec.classes.State import State
from gen_tech_spec.prompts.prompt import DIAGRAM_CODE_GENERATOR_SYSTEM_PROMPT, DIAGRAM_CODE_GENERATOR_HUMAN_PROMPT

def generate_code(state : State):
    """Generate python code using Diagrams library"""

    code = llm.invoke([
        SystemMessage(content=DIAGRAM_CODE_GENERATOR_SYSTEM_PROMPT),
        HumanMessage(content=DIAGRAM_CODE_GENERATOR_HUMAN_PROMPT.format(requirements=state['requirements'], components=state['components']))
    ])

    return {"code" : code.content}