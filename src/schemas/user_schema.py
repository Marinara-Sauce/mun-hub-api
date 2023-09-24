from pydantic import BaseModel


class AdminUserBase(BaseModel):
    username: str


class AdminUserCreate(AdminUserBase):
    password: str


class AdminUser(AdminUserBase):
    user_id: int

    first_name: str
    last_name: str
    super_user: bool = False
    
    class Config:
        from_attributes = True
