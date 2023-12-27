import logging
import uvicorn

from fastapi import FastAPI

from app.api import router
from app.settings import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)

app = FastAPI(debug=True)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
