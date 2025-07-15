# Prompts for AI Report Generation

# System prompt for orchestrator (report planning)
PLANNER_SYSTEM_PROMPT = (
    "A report is a formal document that presents factual information, analysis, and potentially recommendations about a specific topic, event, or situation. "
    "It's a structured way to communicate details and insights to an audience, often in a written format. "
    "Generate a report for the given topic. "
    "The report should be in a structured format with sections and sub-sections. "
    "The report should be in a clear and concise manner. "
    "The report should be in a professional and academic tone. "
)

# Human prompt for orchestrator (injects topic)
def planner_human_prompt(topic):
    return f"here is the report topic: {topic}"

# System prompt for human review (report structure)
HUMAN_REVIEW_SYSTEM_PROMPT = (
    "You are going to get a user response to list of sections that will be generated as part of a report. Verify if user_added_inputs are in sync with the suggested_list_of_sections. Return True or False"
)

def human_review_human_prompt(sections, user_added_inputs): 
   return f"here is the suggested_list_of_sections : {sections} \n\n here is the user_additional_inputs: {user_added_inputs}"

# System prompt for worker (writing a section)
WORKER_SYSTEM_PROMPT = (
    "Write a report section following the provided name and description. "
    "Include no preamble for each section. Use markdown formatting. "
    "See if you can add citations from respective sources."
)

# Human prompt for worker (injects section name and description)
def worker_human_prompt(section_name, section_description):
    return (
        f"Write a report section with the following name: {section_name} "
        f"and description: {section_description}"
    )
