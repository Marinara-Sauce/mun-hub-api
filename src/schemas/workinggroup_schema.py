from pydantic import BaseModel
from src.schemas.delegation_schema import Delegation

# Working Group
class WorkingGroupBase(BaseModel):
    working_group_name: str

class WorkingGroupCreate(WorkingGroupBase):
    pass

class WorkingGroup(WorkingGroupBase):
    working_group_id: int
    delegations: list[Delegation]

    class Config:
        orm_mode = True