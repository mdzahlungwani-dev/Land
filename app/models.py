import uuid
from sqlalchemy import Column, String, Float, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    event_type = Column(String)
    metadata = Column(JSON)
    emotional_weight = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Goal(Base):
    __tablename__ = "goals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    title = Column(String)
    description = Column(String)
    priority = Column(Float)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
