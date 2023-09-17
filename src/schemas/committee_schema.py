from pydantic import BaseModel
from src.schemas.workingpaper_schema import WorkingPaper

from src.models.models import CommitteeSessionTypes
from src.schemas.participant_schema import Participant


class CommitteeBase(BaseModel):
    committee_name: str
    committee_abbreviation: str


class CommitteeCreate(CommitteeBase):
    pass


class Committee(CommitteeBase):
    committee_id: int

    # default values
    committee_announcement: str = ""
    committee_description: str = "No description."
    committee_status: CommitteeSessionTypes = CommitteeSessionTypes.OUT_OF_SESSION

    participants: list[Participant] = []
    working_papers: list[WorkingPaper] = []

    class Config:
        orm_mode = True
