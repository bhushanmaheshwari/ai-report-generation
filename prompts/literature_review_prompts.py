# Prompts for AI Literature Review Generation

# System prompt for orchestrator (literature review planning)
PLANNER_SYSTEM_PROMPT = (
    "A literature review is a comprehensive survey of scholarly sources on a specific topic. "
    "It provides an overview of current knowledge, identifies gaps, and synthesizes findings from multiple studies. "
    "A literature review should critically analyze and evaluate existing research, not just summarize it. "
    "Generate a structured literature review for the given topic. "
    "The review should include sections such as introduction, thematic analysis, methodology comparison, "
    "findings synthesis, research gaps, and conclusions. "
    "The review should be analytical, critical, and comprehensive. "
    "Maintain an objective academic tone throughout."
)

# Human prompt for orchestrator (injects topic)
def planner_human_prompt(topic):
    return f"here is the literature review topic: {topic}"

# System prompt for human review (report structure)
HUMAN_REVIEW_SYSTEM_PROMPT = (
    "You are going to get a user response to list of sections that will be generated as part of a report. Verify if user_added_inputs are in sync with the suggested_list_of_sections. Return True or False"
)

def human_review_human_prompt(sections, user_added_inputs): 
   return f"here is the suggested_list_of_sections : {sections} \n\n here is the user_additional_inputs: {user_added_inputs}"


# System prompt for worker (writing a literature review section)
WORKER_SYSTEM_PROMPT = (
    "Write a literature review section following the provided name and description. "
    "Focus on critical analysis and synthesis of existing research rather than just summary. "
    "Include no preamble for each section. Use markdown formatting. "
    "Incorporate relevant citations and references from academic sources. "
    "Identify patterns, themes, controversies, and gaps in the literature. "
    "Compare and contrast different studies and their methodologies. "
    "Maintain a critical and analytical perspective throughout."
)

# Human prompt for worker (injects section name and description)
def worker_human_prompt(section_name, section_description):
    return (
        f"Write a literature review section with the following name: {section_name} "
        f"and description: {section_description}. "
        f"Focus on critical analysis, synthesis of findings, and identification of research gaps."
    )

# System prompt for synthesizer (combining literature review sections)
LITERATURE_REVIEW_SYNTHESIZER_SYSTEM_PROMPT = (
    "Combine the provided literature review sections into a cohesive and comprehensive literature review. "
    "Ensure smooth transitions between sections and maintain consistency in tone and style. "
    "Add cross-references between sections where appropriate. "
    "Verify that the review maintains a critical and analytical perspective throughout. "
    "Ensure proper academic formatting and citation style. "
    "The final review should demonstrate synthesis of knowledge and identify future research directions."
)

# Human prompt for synthesizer
def literature_review_synthesizer_human_prompt(topic, sections):
    sections_text = "\n\n".join([f"## {section['name']}\n{section['content']}" for section in sections])
    return (
        f"Combine these literature review sections into a comprehensive literature review on: {topic}\n\n"
        f"{sections_text}\n\n"
        f"Ensure the review is cohesive, maintains critical analysis, and identifies research gaps and future directions."
    )

# Additional prompts for specific literature review components

# Prompt for identifying research gaps
RESEARCH_GAPS_PROMPT = (
    "Identify and analyze research gaps in the provided literature. "
    "Look for areas where knowledge is limited, methodologies are lacking, "
    "or where contradictory findings exist. "
    "Suggest potential future research directions based on these gaps."
)

# Prompt for methodology comparison
METHODOLOGY_COMPARISON_PROMPT = (
    "Compare and contrast the methodologies used in the reviewed studies. "
    "Analyze the strengths and weaknesses of different approaches. "
    "Identify methodological trends and innovations in the field. "
    "Discuss how methodological choices may have influenced findings."
)

# Prompt for theoretical framework analysis
THEORETICAL_FRAMEWORK_PROMPT = (
    "Analyze the theoretical frameworks used in the reviewed literature. "
    "Identify dominant theories and emerging theoretical perspectives. "
    "Discuss how different theoretical approaches contribute to understanding the topic. "
    "Highlight any theoretical gaps or conflicts in the literature."
)
