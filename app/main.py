from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Strumento
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres:postgres@db-postgres:5432/registrydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # oppure ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/strumenti")
def get_strumenti():
    db = SessionLocal()
    strumenti = db.query(Strumento).all()
    db.close()
    return strumenti

@app.post("/strumenti")
def add_strumento(payload: dict):
    db = SessionLocal()
    nuovo = Strumento(**payload)
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    db.close()
    return {"status": "aggiunto"}