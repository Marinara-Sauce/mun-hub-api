from pydantic import BaseModel

class ParticipantBase(BaseModel):
    country_alpha_2: str


class ParticipantCreate(ParticipantBase):
    delegation_id: int
    committee_id: str


class Participant(ParticipantBase):
    participant_id: int
    
    class Config:
        orm_mode = True


