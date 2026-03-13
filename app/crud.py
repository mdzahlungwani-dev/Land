from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, email: str):
    user = models.User(email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def create_event(db: Session, event):

    db_event = models.Event(
        user_id=event.user_id,
        event_type=event.event_type,
        metadata=event.metadata,
        emotional_weight=event.emotional_weight
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def create_goal(db: Session, goal):

    db_goal = models.Goal(
        user_id=goal.user_id,
        title=goal.title,
        description=goal.description,
        priority=goal.priority,
        status=goal.status
    )

    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)

    return db_goal
