from sqlalchemy.orm import Session
import logging

from app.models import User
from app.schemas.schemas_user import UserCreate, UserModify


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password, name=user.name)
    db.add(db_user)
    # 使用 flush 将用户数据写入数据库，但事务仍然处于打开状态
    db.flush()
    return db_user


def modify_user(db: Session, user: UserModify):
    logger = logging.getLogger()
    rows = db.query(User).filter(User.id == user.id).update({"name": user.name}, synchronize_session=False)
    logger.info(rows)
