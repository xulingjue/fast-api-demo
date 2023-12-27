from fastapi import Header, HTTPException
from app.settings import QUERY_TOKEN, X_TOKEN


async def get_token_header(x_token: str = Header()):
    if x_token != X_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
