from pydantic import BaseModel
from src.models.models import WorkingGroup

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