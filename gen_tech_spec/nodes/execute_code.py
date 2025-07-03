from langchain.tools import tool
import tempfile
from pathlib import Path
import subprocess

from gen_tech_spec.classes.State import State

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

@tool
def generate_architecture_diagram(code: str) -> str:
    """
    Executes Python code using diagrams lib to generate a PNG diagram.
    Returns the diagram as PNG bytes.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        script_path = tmpdir_path / "diagram_code.py"
        output_path = tmpdir_path / "output.png"

        # Save code to file
        with open(script_path, "w") as f:
            f.write(code)

        # Execute the diagram code (which saves output.png)
        try:
            subprocess.run(["python", str(script_path)], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error executing diagram code: {e}")

        if not output_path.exists():
            raise FileNotFoundError("Diagram PNG was not generated.")

        # Read the image
        return output_path


def execute_code(state: State):
    # image_path = generate_architecture_diagram.invoke({"code": state['code']})
    image_path = "gen_tech_spec/static/images/sample_diagram.png" 
    return { "diagram": image_path }

