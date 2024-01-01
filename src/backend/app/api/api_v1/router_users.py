import logging
import time

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.api.depends import get_token_header
from app.crud import crud_user
from app.db import get_db, redis_client

from app.api.decorators import log_request

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["users"])
@log_request
def read_users(user_id: int):
    logger = logging.getLogger()
    redis_client.set("user.email", "229533398@qq.com", 60)
    logger.info(redis_client.get("user.email"))
    logger.info('请求时间：%s ,用户Id：%d' % (time.strftime("%A, %d. %B %Y %I:%M:%S %p"), user_id))
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
