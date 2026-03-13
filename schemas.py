from pydantic import BaseModel
from typing import Optional, Dict


class EventCreate(BaseModel):
    user_id: str
    event_type: str
    metadata: Dict
    emotional_weight: Optional[float]


class GoalCreate(BaseModel):
    user_id: str
    title: str
    description: str
    priority: float
    status: str


class UserCreate(BaseModel):
    email: str
