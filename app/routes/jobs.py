from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.job import Job

router = APIRouter(prefix="/jobs")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_job(company: str, position: str, status: str = "Applied", notes: str = "", db: Session = Depends(get_db)):
    job = Job(company=company, position=position, status=status, notes=notes)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if job:
        db.delete(job)
        db.commit()
    return {"deleted": True}
