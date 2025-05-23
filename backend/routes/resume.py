from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Resume

router = APIRouter(prefix="/resume", tags=["resume"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_resume(user_id: int, title: str, content: str, db: Session = Depends(get_db)):
    resume = Resume(user_id=user_id, title=title, content=content)
    db.add(resume)
    db.commit()
    return {"msg": "Resume created"}
