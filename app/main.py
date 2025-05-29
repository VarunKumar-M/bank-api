from fastapi import FastAPI
from .database import Base, engine
from .routers import bank

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank API")

app.include_router(bank.router)