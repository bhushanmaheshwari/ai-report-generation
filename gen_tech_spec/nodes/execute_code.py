from langchain.tools import tool
import tempfile
from pathlib import Path
import subprocess
from graphviz import Source
from gen_tech_spec.classes.State import State
import os
import uuid
import re

OUTPUT_DIR = "gen_tech_spec/static/diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_dot_code(code: str) -> str:
    """
    Removes triple backticks and optional language tags (e.g., ```dot, ```python) from the LLM output.
    Returns only the code inside the first code block, or the original string if no code block is found.
    """
    match = re.search(r"```[a-zA-Z0-9]*\s*\n(.*?)```", code, re.DOTALL)
    if match:
        return match.group(1).strip()
    return code.strip()

def generate_architecture_diagram(code: str) -> str:
    """
    Executes Python code using graphviz lib to generate a PNG diagram.
    Returns the image file path.
    """
    diagram_id = str(uuid.uuid4())
    script_path = os.path.join(OUTPUT_DIR, f"{diagram_id}.dot")
    #output_file_name = os.path.join(OUTPUT_DIR, f"{diagram_id}")
    #output_path = os.path.join(OUTPUT_DIR, f"{diagram_id}.png")

    # Save code to file
    with open(script_path, "w") as f:
        f.write(code)

    try:
        src = Source(code, filename=script_path, format="png")
        src.render(cleanup=True)
    except Exception as e:
        raise RuntimeError(f"Error executing diagram code: {e}")
    
    # Read the image
    return script_path + '.png'


def execute_code(state: State):
    clean_code = clean_dot_code(state['code'])
    image_path = generate_architecture_diagram(clean_code)
    return { "diagram": image_path }

