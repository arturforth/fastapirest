from sqlalchemy.orm import Session
from schemas import schemas
from models import models


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_client_by_name(db: Session, client_name: str):
    return db.query(models.Client).filter(models.Client.name == client_name).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.Client):
    db_client = models.Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_client_account(db: Session, account: schemas.Account, client_id: int):
    db_account = models.Account(**account.dict(), client_id=client_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
