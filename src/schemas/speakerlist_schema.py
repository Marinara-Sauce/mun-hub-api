from pydantic import BaseModel

from src.schemas.committee_schema import Committee


# speaker list

class SpeakerListEntryBase(BaseModel):
    speakerlistentry_id: str


class SpeakerListEntryCreate(SpeakerListEntryBase):
    pass


class SpeakerListEntry(SpeakerListEntryBase):
    speakerlist_id: str
    participant_id: str

    speakerlist: SpeakerList

    class Config:
        orm_mode = True


class SpeakerListBase(BaseModel):
    speakerlist_name: str


class SpeakerListCreate(SpeakerListBase):
    pass


class SpeakerList(SpeakerListBase):
    speakerlist_id: str
    committee_id: str

    committee: list[Committee] = []
    speakerlistentries: list[SpeakerListEntry] = []

    class Config:
        orm_mode = True


# speaker list ENTRY

