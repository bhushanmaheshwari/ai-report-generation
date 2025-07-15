from workflow import orchestrator_worker
from langgraph.types import Command

class ReportManager:
    """A report manager to review, orchestrate, assign workers, and sythesize the final report"""

    def __init__(self):
        self.config = {"configurable": {"thread_id": "1"}}

    def _process_events(self, events):
        divider = "\n\n---\n\n"
        for event in events:
            if "planner" in event:
                yield "**Proposed report layout:**\n\n"
                for section in event["planner"]["sections"]:
                   yield f"- **{section.name}** : {section.description}\n\n"
                yield divider
                
            elif '__interrupt__' in event:
                yield "Please review the sections of the report and provide your feedback"
                yield "__interrupt__"

            elif 'human_review' in event:
                yield f"**Human In The Loop** - {event['human_review']['human_message']}"
                yield divider
   
            elif "worker" in event:
                yield "\n\n**Writing:** "
                yield event['worker']['section_summaries'][0]
                
            elif "synthesizer" in event:
                yield divider
                yield "# Final Report"
                yield "\n\n"
                yield event["synthesizer"]["final_report"]
                yield divider


    def run(self, topic):
        yield "*Jump Starting Agent...*\n\n"
        events = orchestrator_worker.stream(
            {"topic": topic},
            self.config,
            stream_mode="updates"
        )
        yield from self._process_events(events)
        
    def resume(self, user_added_inputs:str):
        yield "\n\n*Resuming Agent...*\n\n"
        events = orchestrator_worker.stream(
            Command(resume=user_added_inputs),
            config=self.config,
            stream_mode="updates"
        )
        yield from self._process_events(events)