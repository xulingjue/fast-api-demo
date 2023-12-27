from pydantic import BaseModel


# from app.models import Item


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserModify(UserBase):
    id: int


class User(UserBase):
    id: int
    is_active: bool

    # items: list[Item] = []

    class Config:
        from_attributes = True
