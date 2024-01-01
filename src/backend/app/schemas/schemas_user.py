from pydantic import BaseModel, field_validator


class UserBase(BaseModel):
    name: str
    email: str

    @field_validator('name')
    def name_must_contain_1(cls, v):
        '''
        参数校验示例
        '''
        if 1 not in v:
            raise ValueError('must contain a space')
        return v.title()


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
