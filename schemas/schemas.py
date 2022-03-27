import datetime
from typing import Optional
from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[int]
    available_amount: float
    # client_id: int

    class Config:
        orm_mode = True


class MovementDetail(BaseModel):
    id: int
    type: str
    amount: float
#     move_id: int
#
#     class Config:
#         orm_mode = True


class Movement(BaseModel):
    id: int
    date: datetime.date
    # client_id: int
    # move_details: Optional[MovementDetail]

    class Config:
        orm_mode = True


class Client(BaseModel):
    id: Optional[int]
    name: str
    accounts: Optional[Account]
    # movements: Optional[Movement]

    class Config:
        orm_mode = True

