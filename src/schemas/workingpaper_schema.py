from typing import Optional
from pydantic import BaseModel
from src.schemas.workinggroup_schema import WorkingGroup

# Working Papers
class WorkingPaperBase(BaseModel):
    paper_link: str

class WorkingPaperCreate(WorkingPaperBase):
    pass

class WorkingPaper(WorkingPaperBase):
    working_paper_id: int
    working_group: WorkingGroup

    class Config:
        orm_mode = True