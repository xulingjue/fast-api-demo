from app.api.api_v1 import router_items, router_login, router_users
from fastapi import APIRouter

router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)

router.include_router(router_items.router)
router.include_router(router_login.router)
router.include_router(router_users.router)
