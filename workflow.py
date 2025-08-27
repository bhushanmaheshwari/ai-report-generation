import uuid
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

from nodes.planner import planner
from nodes.orchestrator import orchestrator, assign_workers
from nodes.human_review import human_review, human_decision
from nodes.worker import worker
from nodes.synthesizer import synthesizer

from functools import partial

from classes.State import State, WorkerState

in_memory_store = InMemoryStore()
checkpointer = InMemorySaver()

user_id = '1'
namespace_for_memory = (user_id, "memories")

memory_id = str(uuid.uuid4())
memory = {"content_preference":  "I am Akash, and I always like content to be in a poem format!"}

in_memory_store.put(namespace_for_memory, memory_id, {"memory": memory})

orchestrator_worker_builder = StateGraph(State)

orchestrator_worker_builder.add_node("planner", planner)
orchestrator_worker_builder.add_node("orchestrator", orchestrator)
orchestrator_worker_builder.add_node(
    "worker",
    partial(worker, store=in_memory_store)
)
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


orchestrator_worker = orchestrator_worker_builder.compile(checkpointer=checkpointer, store=in_memory_store)