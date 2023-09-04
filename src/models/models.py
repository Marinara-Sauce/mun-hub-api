import enum

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from src.database.database import Base


class CommitteeSessionTypes(enum.Enum):
    """
    Different types of committee sessions.
    """
    IN_SESSION = 1
    SUSPENDED_SESSION = 2
    OUT_OF_SESSION = 3
    UNMOD = 4
    MOD = 5


class Participant(Base):
    __tablename__ = "participants"

    # ids
    participant_id = Column(Integer, primary_key=True, index=True, unique=True)

    # foreign ids
    delegation_id = Column(Integer, ForeignKey("delegations.delegation_id"))
    committee_id = Column(Integer, ForeignKey("committees.committee_id"))

    # relationships
    delegation = relationship("Delegation", back_populates="participants")
    committee = relationship("Committee", back_populates="participants")

    # country information (use ISO database to get any additional information)
    country_alpha_2 = Column(String, primary_key=True, index=True)


class Committee(Base):
    __tablename__ = "committees"

    # id
    committee_id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)

    # participants in delegation
    participants = relationship("Participant", back_populates="committee")
    speakerlists = relationship("SpeakerList", back_populates="committee")

    # data
    committee_name = Column(String)
    committee_abbreviation = Column(String)
    committee_description = Column(String)
    committee_status = Column(Enum(CommitteeSessionTypes))


class Delegation(Base):
    __tablename__ = "delegations"

    # id
    delegation_id = Column(Integer, primary_key=True, index=True, unique=True)

    # participants in delegation
    participants = relationship("Participant", back_populates="delegation")

    # data
    delegation_name = Column(String)


class SpeakerList(Base):
    __tablename__ = "speakerlists"

    # id
    speakerlist_id = Column(Integer, primary_key=True, index=True, unique=True)

    # foreign ids
    committee_id = Column(Integer, ForeignKey("committees.committee_id"))

    # data
    speakerlist_name = Column(String)

    # relationships
    committee = relationship("Committee", back_populates="speakerlists")
    speakerlistentries = relationship("SpeakerListEntry", back_populates="speakerlist")


class SpeakerListEntry(Base):
    __tablename__ = "speakerlistentries"

    # id
    speakerlistentry_id = Column(Integer, primary_key=True, index=True, unique=True)

    # foreign ids
    speakerlist_id = Column(Integer, ForeignKey("speakerlists.speakerlist_id"))
    participant_id = Column(Integer, ForeignKey("participants.participant_id"))

    # relationships
    speakerlist = relationship("SpeakerList", back_populates="speakerlistentries")
