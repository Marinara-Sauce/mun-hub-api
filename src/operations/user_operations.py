from typing import Optional
from requests import Session
from src.models.models import AdminUser


# get user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(AdminUser).filter(AdminUser.user_id == user_id).first()


# get user by username
def get_user_by_username(db: Session, username: str) -> Optional[AdminUser]:
    return db.query(AdminUser).filter(AdminUser.username == username).first()