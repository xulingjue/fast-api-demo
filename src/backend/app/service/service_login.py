from sqlalchemy.orm import Session
from app.models import User


def login(db: Session, user_id: int) -> User:
    '''
    登录示例
    '''
    pass
