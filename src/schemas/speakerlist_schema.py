from pydantic import BaseModel

from src.schemas.committee_schema import Committee

# speaker list ENTRY

class SpeakerListEntryBase(BaseModel):
    speakerlistentry_id: str


class SpeakerListEntryCreate(SpeakerListEntryBase):
    pass


class SpeakerListEntry(SpeakerListEntryBase):
    speakerlist_id: str
    participant_id: str

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
    speakerlist_entries: list[SpeakerListEntry] = []

    class Config:
        orm_mode = True
