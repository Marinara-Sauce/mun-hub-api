from pydantic import BaseModel
from src.schemas.delegation_schema import Delegation
from src.schemas.workingpaper_schema import WorkingPaper

from src.models.models import CommitteePollingTypes, CommitteeSessionTypes

class CommitteeBase(BaseModel):
    committee_name: str
    committee_abbreviation: str


class CommitteeCreate(CommitteeBase):
    pass


class CommitteeUpdate(CommitteeBase):
    committee_id: int
    ommittee_announcement: str = ""
    committee_description: str = ""
    committee_status: CommitteeSessionTypes = CommitteeSessionTypes.OUT_OF_SESSION


class Committee(CommitteeBase):
    committee_id: int

    # default values
    committee_announcement: str = ""
    committee_description: str = "No description."
    committee_status: CommitteeSessionTypes = CommitteeSessionTypes.OUT_OF_SESSION
    committee_poll: CommitteePollingTypes = CommitteePollingTypes.NONE

    delegations: list[Delegation] = []
    working_papers: list[WorkingPaper] = []

    class Config:
        from_attributes = True
