from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/banks/", response_model=list[schemas.BankResponse])
def read_banks(db: Session = Depends(get_db)):
    return crud.get_all_banks(db)

@router.get("/branches/", response_model=list[schemas.BranchResponse])
def read_branch(ifsc: str = None, branch: str = None, db: Session = Depends(get_db)):
    if ifsc:
        branch_obj = crud.get_branch_by_ifsc(db, ifsc)
        if not branch_obj:
            raise HTTPException(status_code=404, detail="Branch not found")
        return [branch_obj]
    elif branch:
        return crud.get_branch_by_name(db, branch)
    else:
        raise HTTPException(status_code=400, detail="Provide IFSC or Branch name")