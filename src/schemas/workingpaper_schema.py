from pydantic import BaseModel
from models.models import Committee, WorkingGroup

# Working Papers
class WorkingPaperBase(BaseModel):
    committee: Committee
    paper_link: str

class WorkingPaperCreate(WorkingPaperBase):
    pass

class WorkingPaper(WorkingPaperBase):
    working_paper_id: int

    working_group: WorkingGroup

    class Config:
        orm_mode = True