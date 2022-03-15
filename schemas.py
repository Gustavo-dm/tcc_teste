from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    product: str
    description: str
    status: str
    email: str
    phone: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    client_id: int
    status: str

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    email: str
    phone: str
    full_name = str


class ClientCreate(BaseModel):
    pass


class Client(BaseModel):
    id: int
    orders: list[Order] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(BaseModel):
    hashed_password: str


class User(BaseModel):
    id: int
    is_active: bool
    is_admin: bool
