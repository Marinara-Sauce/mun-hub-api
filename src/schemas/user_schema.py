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
    super_user: bool = False
    
    class Config:
        from_attributes = True
