from fastapi import Header, HTTPException, Depends
from typing import Annotated, Generator
from sqlmodel import Session
from app.db.engine import engine


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


def get_db() -> Generator:
    '''
    sqlmodel链接
    '''
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
