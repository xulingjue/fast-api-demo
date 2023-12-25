import logging, uvicorn
from fastapi import Depends, FastAPI

from app.api.api_v1 import users, items
from app.api.deps import get_query_token, get_token_header
from .internal import admin
from .settings import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
