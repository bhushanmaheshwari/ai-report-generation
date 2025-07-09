import tempfile
from pathlib import Path
import subprocess

dummy_code = """
from diagrams import Diagram, Cluster, Edge, Node

with Diagram("Travel Management System", show=False, filename="output"):
    users = Node("Users")

    with Cluster("Azure Cloud"):
        with Cluster("Resource Group"):
            with Cluster("Azure Kubernetes Service (AKS)"):
                frontend_pod = Node("Frontend (React, TypeScript)")
                backend_pod = Node("Backend (Node.js, Express.js)")

            postgres = Node("PostgreSQL Database")
            api_management = Node("API Management")
            active_directory = Node("Azure Active Directory")
            blob_storage = Node("Blob Storage (Itinerary Attachments)")


    with Cluster("External Systems"):
        travel_apis = Node("Travel APIs (Flights, Hotels, Cars)")
        expense_system = Node("Expense Management System")

    with Cluster("Monitoring"):
        grafana = Node("Grafana")
        prometheus = Node("Prometheus")

    users >> Edge(label="User Authentication") >> active_directory
    users >> Edge(label="Web UI") >> api_management
    api_management >> frontend_pod
    frontend_pod >> backend_pod
    backend_pod >> postgres
    backend_pod >> blob_storage
    backend_pod >> Edge(label="API Calls") >> travel_apis
    backend_pod >> Edge(label="Expense Data") >> expense_system

    prometheus >> grafana
    frontend_pod - Edge(style="dashed", label="Metrics") - prometheus
    backend_pod - Edge(style="dashed", label="Metrics") - prometheus
    postgres - Edge(style="dashed", label="Metrics") - prometheus

    Node("Azure DevOps (CI/CD)") >> Node

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