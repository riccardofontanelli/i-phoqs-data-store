from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Strumento
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://registrydb_vf8t_user:NS7Rrp3FdjoUHuPNBKdYxXKTi10G6tXj@dpg-d0156gq4d50c73cs9e20-a.frankfurt-postgres.render.com/registrydb_vf8t"

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

@app.get("/")
def read_root():
    return {"message": "Data Store online!"}

@app.delete("/strumenti/{id}")
def delete_strumento(id: int):
    db = SessionLocal()
    strumento = db.query(Strumento).filter(Strumento.id == id).first()
    if not strumento:
        db.close()
        raise HTTPException(status_code=404, detail="Strumento non trovato")
    db.delete(strumento)
    db.commit()
    db.close()
    return {"status": "eliminato"}