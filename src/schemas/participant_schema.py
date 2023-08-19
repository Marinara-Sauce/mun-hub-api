from pydantic import BaseModel


class ParticipantBase(BaseModel):
    country_alpha_2: str


class ParticipantCreate(ParticipantBase):
    delegation_id: str
    committee_id: str


class Participant(ParticipantBase):
    participant_id: str

    class Config:
        orm_mode = True


