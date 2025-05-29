from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Bank, Branch

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/banks")
def get_banks(db: Session = Depends(get_db)):
    return db.query(Bank).all()

@router.get("/branches")
def get_branches(db: Session = Depends(get_db)):
    return db.query(Branch).all()

@router.get("/ifsc/{code}")
def get_branch_by_ifsc(code: str, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.ifsc == code).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch
