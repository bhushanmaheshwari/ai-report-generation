from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

from gen_report.nodes.planner import planner
from gen_report.nodes.orchestrator import orchestrator, assign_workers
from gen_report.nodes.human_review import human_review, human_decision
from gen_report.nodes.worker import worker
from gen_report.nodes.synthesizer import synthesizer

from gen_report.classes.State import State, WorkerState


orchestrator_worker_builder = StateGraph(State)

orchestrator_worker_builder.add_node("planner", planner)
orchestrator_worker_builder.add_node("orchestrator", orchestrator)
orchestrator_worker_builder.add_node("worker", worker)
orchestrator_worker_builder.add_node("synthesizer", synthesizer)
orchestrator_worker_builder.add_node("human_review", human_review)

orchestrator_worker_builder.add_edge(START, "planner")
orchestrator_worker_builder.add_edge("planner", "human_review")
orchestrator_worker_builder.add_conditional_edges(
    "human_review", human_decision, ["orchestrator", "planner"]
)
orchestrator_worker_builder.add_conditional_edges(
    "orchestrator", assign_workers, ["worker"]
)
orchestrator_worker_builder.add_edge("worker", "synthesizer")
orchestrator_worker_builder.add_edge("synthesizer", END)

memory = MemorySaver()
orchestrator_worker = orchestrator_worker_builder.compile(checkpointer=memory)