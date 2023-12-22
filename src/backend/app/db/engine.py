'''
sqlmodel 连接
'''
from sqlmodel import create_engine

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
