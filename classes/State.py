from typing import Annotated, List, TypedDict
from classes.Sections import Section
import operator

class State(TypedDict):
    topic: str
    sections: List[Section]
    section_summaries: Annotated[list, operator.add]
    completed_sections: Annotated[list, operator.add]
    final_report: str

class WorkerState(TypedDict):
    section_summaries: Annotated[list, operator.add]
    completed_sections: Annotated[list, operator.add]