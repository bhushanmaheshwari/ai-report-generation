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

    dummy_code = """
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=False):
    source = EKS("k8s source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        queue = SQS("event queue")

        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]

    store = S3("events store")
    dw = Redshift("analytics")

    source >> workers >> queue >> handlers
    handlers >> store
    handlers >> dw

    """
    return {"code" : code.content, "dummy_code": dummy_code}