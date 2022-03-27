from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from config.db import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    accounts = relationship('Account', back_populates='client')
    movements_ids = relationship('Movement', back_populates='client')


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    available_amount = Column(Float)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship('Client', back_populates='accounts')


class Movement(Base):
    __tablename__ = 'movements'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship('Client', back_populates='movements_ids')
    movements_details_ids = relationship('MovementDetail', back_populates='move2')


class MovementDetail(Base):
    __tablename__ = 'movements_detail'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(16))
    amount = Column(Float)
    movement_id = Column(Integer, ForeignKey('movements.id'))

    move2 = relationship('Movement', back_populates='movements_details_ids')
