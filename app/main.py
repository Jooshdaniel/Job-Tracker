from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import jobs

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker")

app.include_router(jobs.router)
