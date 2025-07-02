# Prompts for AI Report Generation

# System prompt for orchestrator (report planning)
ORCHESTRATOR_SYSTEM_PROMPT = (
    "A report is a formal document that presents factual information, analysis, and potentially recommendations about a specific topic, event, or situation. "
    "It's a structured way to communicate details and insights to an audience, often in a written format. "
    "Generate a report for the given topic."
)

# Human prompt for orchestrator (injects topic)
def orchestrator_human_prompt(topic):
    return f"here is the report topic: {topic}"

# System prompt for worker (writing a section)
WORKER_SYSTEM_PROMPT = (
    "Write a report section following the provided name and description. "
    "Include no preamble for each section. Use markdown formatting. "
    "See if you can cite the resources from respective sources, and add a hyperlink to each citation."
)

# Human prompt for worker (injects section name and description)
def worker_human_prompt(section_name, section_description):
    return (
        f"Write a report section with the following name: {section_name} "
        f"and description: {section_description}"
    )
