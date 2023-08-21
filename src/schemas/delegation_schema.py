from pydantic import BaseModel

from src.schemas.participant_schema import Participant


class DelegationBase(BaseModel):
    delegation_name: str


class DelegationCreate(DelegationBase):
    pass


class Delegation(DelegationBase):
    delegation_id: int
    participants: list[Participant] = []

    class Config:
        orm_mode = True
