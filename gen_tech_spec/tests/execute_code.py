import tempfile
from pathlib import Path
import subprocess

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

def generate_architecture_diagram(code: str) -> str:
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


generate_architecture_diagram(dummy_code)