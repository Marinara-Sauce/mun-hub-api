from pydantic import BaseModel

from schemas.participant_schema import Participant


class DelegationBase(BaseModel):
    delegation_name: str


class DelegationCreate(DelegationBase):
    pass


class Delegation(DelegationBase):
    delegation_id: str
    participants: list[Participant] = []

    class Config:
        orm_mode = True
