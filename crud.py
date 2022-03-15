from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    not_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=not_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_order_by_client(db: Session, client_id: str):
    return db.query(models.Order).filter(models.Order.client_id == client_id).all()


def get_all_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Orders).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate, client_id: int):
    db_order = models.Item(**item.dict(), client_id=client_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_item)
    return db_item
