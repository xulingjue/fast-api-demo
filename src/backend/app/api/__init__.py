from app.api.api_v1 import router as api_v1_router
from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

router.include_router(api_v1_router)
