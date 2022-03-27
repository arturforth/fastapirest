from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud
from models import models
from schemas import schemas
from config.db import SessionLocal, engine
# from schemas.schemas import Client

models.Base.metadata.create_all(bind=engine)

client = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@client.get('/clients')
def get_clients():
    # return con.execute(Client.select()).fetchall()
    return None


@client.post('/clients/', response_model=schemas.Client)
def create_users(client: schemas.Client, db: Session = Depends(get_db)):
    db_user = crud.get_client_by_name(db, client_name=client.name)
    if db_user:
        raise HTTPException(status_code=400, detail='Client already registered')

    return crud.create_client(db, client=client)
