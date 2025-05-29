from pydantic import BaseModel

class BankBase(BaseModel):
    name: str

class BankResponse(BankBase):
    id: int
    class Config:
        orm_mode = True

class BranchBase(BaseModel):
    ifsc: str
    branch: str
    address: str
    city: str
    district: str
    state: str

class BranchResponse(BranchBase):
    id: int
    bank: BankResponse
    class Config:
        orm_mode = True