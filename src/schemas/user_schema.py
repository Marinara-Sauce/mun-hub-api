from pydantic import BaseModel


class AdminUserBase(BaseModel):
    username: str
    password: str


class AdminUserCreate(AdminUserBase):
    pass


class AdminUser(AdminUserBase):
    user_id: int

    first_name: str
    last_name: str

    class Config:
        orm_mode = True