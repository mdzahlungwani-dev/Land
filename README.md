# Life OS

Experimental backend for a Personal Adaptive Life Operating System.

Built with:

FastAPI
PostgreSQL
SQLAlchemy
Docker

## Run locally

1 Install dependencies

pip install -r requirements.txt

2 Start Postgres

docker-compose up

3 Run API

uvicorn app.main:app --reload

## API Docs

http://localhost:8000/docs
