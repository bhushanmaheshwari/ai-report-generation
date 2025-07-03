from gen_report.classes.State import State

def synthesizer(state: State):
    """Synthesize fill report from sections"""

    completed_sections = state["completed_sections"]
    completed_report_sections = "\n\n---\n\n".join(completed_sections)

    return {"final_report": completed_report_sections}