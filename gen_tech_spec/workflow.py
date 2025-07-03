from langgraph.graph import StateGraph, START, END
from gen_tech_spec.classes.State import State

from gen_tech_spec.nodes.refine_requirements import refine_requirements
from gen_tech_spec.nodes.generate_tech_stack import generate_tech_stack
from gen_tech_spec.nodes.generate_code import generate_code
from gen_tech_spec.nodes.execute_code import execute_code
from gen_tech_spec.nodes.generate_document import generate_document


workflow = StateGraph(State)

workflow.add_node("refine_requirements", refine_requirements)
workflow.add_node("generate_tech_stack", generate_tech_stack)
workflow.add_node("generate_code", generate_code)
workflow.add_node("execute_code", execute_code)
workflow.add_node("generate_document", generate_document)

workflow.add_edge(START, "refine_requirements")
workflow.add_edge("refine_requirements", "generate_tech_stack")
workflow.add_edge("generate_tech_stack", "generate_code")
workflow.add_edge("generate_code", "generate_document")
# workflow.add_edge("generate_code", "execute_code")
# workflow.add_edge("execute_code", "generate_document")
workflow.add_edge("generate_document", END)

chain = workflow.compile()



