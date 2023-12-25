import datetime
import logging

from app.crud import crud_user
from app.db import SessionLocal


def demo_job() -> None:
    try:
        session = SessionLocal()
        users = crud_user.get_users(session)
        for user in users:
            print(user.email)
    finally:
        session.close()

    print("demo_job")
    logging.info('[demo_job] running at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
