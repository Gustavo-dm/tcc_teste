from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    title: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    order: list[Order] = []

    class Config:
        orm_mode = True