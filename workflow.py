from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

from nodes.planner import planner
from nodes.orchestrator import orchestrator, assign_workers
from nodes.human_review import human_review, human_decision
from nodes.worker import worker
from nodes.synthesizer import synthesizer

from classes.State import State, WorkerState


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