from pydantic import BaseModel
from models.models import Committee, Participant, WorkingPaper

# Working Papers
class WorkingGroupBase(BaseModel):
    working_group_name: str

class WorkingGroupCreate(WorkingGroupBase):
    pass

class WorkingGroup(WorkingGroupBase):
    working_group_id: int

    working_paper: WorkingPaper

    working_group_participants: list[Participant] = []

    class Config:
        orm_mode = True