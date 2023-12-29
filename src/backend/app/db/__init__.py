import logging

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import DATABASE_URL

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, pool_size=10
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        logger.info("关闭db")
        db.close()


redis_pool = redis.ConnectionPool(
    host='10.0.74.222',
    port='6055',
    db=0,
    password='6xf0vHzZI$',
    decode_responses=True
)

redis_client = redis.Redis(connection_pool=redis_pool)
