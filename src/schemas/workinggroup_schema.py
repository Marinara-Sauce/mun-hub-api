from pydantic import BaseModel
from src.schemas.participant_schema import Participant

# Working Group
class WorkingGroupBase(BaseModel):
    # working_group_name: str
    pass

class WorkingGroupCreate(WorkingGroupBase):
    pass

class WorkingGroup(WorkingGroupBase):
    working_group_id: int

    working_group_participants: list[Participant] = []

    class Config:
        orm_mode = True