from pydantic import BaseModel
from src.models.models import Participant

# Working Papers
class WorkingGroupBase(BaseModel):
    working_group_name: str

class WorkingGroupCreate(WorkingGroupBase):
    pass

class WorkingGroup(WorkingGroupBase):
    working_group_id: int

    working_group_participants: list[Participant] = []

    class Config:
        orm_mode = True