from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables.config import RunnableConfig
from langchain.storage import InMemoryStore

from llm import llm
from classes.State import WorkerState
from prompt import WORKER_SYSTEM_PROMPT, worker_human_prompt

def worker(state: WorkerState, config:RunnableConfig, *, store:InMemoryStore):
    """Worker writes a section of the report"""

    user_id = config["configurable"]["user_id"]

    # Namespace the memory
    namespace = (user_id, "memories")

    # Search based on the most recent message
    memories = store.search(
        namespace,
        # query=state["messages"][-1].content,
        limit=3
    )

    print(memories)

    
    memories_str = "\n".join([
        str(d.value.get("memory") or d.value.get("content_preference") or d.value)
        for d in memories
    ])
    
    section = llm.invoke(
        [
            SystemMessage(
                content=WORKER_SYSTEM_PROMPT
            ),
            HumanMessage(
                content=worker_human_prompt(state['section'].name, state['section'].description, memories_str)
            )
        ]
    )

    return {
        "section_summaries": [f"{state['section'].name} | {state['section'].description}"],
        "completed_sections": [section.content]
    }