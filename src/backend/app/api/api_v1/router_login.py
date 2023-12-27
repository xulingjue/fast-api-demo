from fastapi import APIRouter, Depends

from app.api.deps import get_token_header

router = APIRouter(
    prefix="/account",
    tags=["account"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def login():
    return ""
