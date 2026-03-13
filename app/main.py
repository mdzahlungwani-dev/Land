from fastapi import FastAPI

from .database import engine
from .models import Base

from .routers import events, goals, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Life OS API")


app.include_router(events.router)
app.include_router(goals.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Life OS running"}
