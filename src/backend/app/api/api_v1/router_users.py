import logging
import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.api.deps import get_token_header
from app.crud import crud_user
from app.db import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["users"])
async def read_users():
    logger = logging.getLogger()
    logger.info('请求时间：%s ' % time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.schemas_user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = crud_user.create_user(db=db, user=user)
    db.commit()
    return db_user


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=schemas.User)
def modify_user(user_id: int, user: schemas.schemas_user.UserModify, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud_user.modify_user(db, user)
    try:
        with db.begin_nested():
            # 开始数据库事务
            # 在事务中执行数据库操作
            # 这里可以添加您的数据库操作逻辑，例如创建用户
            # 如果出现异常，事务将自动回滚
            # 在此示例中，我们简单地将用户名插入到 users 表中
            crud_user.modify_user(db, user)
            raise HTTPException(status_code=404, detail="User not found")
            user.id = 2
            crud_user.modify_user(db, user)
            # 提交最外层事务
            db.commit()
            return db_user
    except Exception:
        # 处理唯一约束冲突的异常
        raise HTTPException(status_code=404, detail="User not found")
