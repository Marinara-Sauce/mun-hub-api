from pydantic import BaseModel

from src.models.models import CommitteeSessionTypes
from src.schemas.participant_schema import Participant


class CommitteeBase(BaseModel):
    committee_name: str
    committee_abbreviation: str


class CommitteeCreate(CommitteeBase):
    pass


class Committee(CommitteeBase):
    committee_id: str

    # default values
    committee_description: str = "No description."
    committee_status: CommitteeSessionTypes = CommitteeSessionTypes.OUT_OF_SESSION

    participants: list[Participant] = []

    class Config:
        orm_mode = True
