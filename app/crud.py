from sqlalchemy.orm import Session
from . import models

def get_all_banks(db: Session):
    return db.query(models.Bank).all()

def get_branch_by_ifsc(db: Session, ifsc: str):
    return db.query(models.Branch).filter(models.Branch.ifsc == ifsc).first()

def get_branch_by_name(db: Session, branch: str):
    return db.query(models.Branch).filter(models.Branch.branch.ilike(f"%{branch}%")).all()