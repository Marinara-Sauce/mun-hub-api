from pydantic import BaseModel


class DelegationBase(BaseModel):
    delegation_name: str


class DelegationCreate(DelegationBase):
    pass


class Delegation(DelegationBase):
    delegation_id: int
