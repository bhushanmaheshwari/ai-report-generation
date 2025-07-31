from typing import List
from pydantic import BaseModel, Field

class Section(BaseModel):
    name: str = Field(
        description="Name for this section of this report"
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section, explaining its purpose. See if you can cite the resources from respective scholarly sources."
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="List of sections to be included in the report for the given topic, each with a name and description"
    )

class HumanApproval(BaseModel):
    approved: bool = Field(
        description="Return True or False based on the user feedback"
    )