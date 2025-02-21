# app/api/items.py
from fastapi import APIRouter, Depends
from typing import List

from app.services import user_service
from app.models.user import User

router = APIRouter()

@router.get("/users/", response_model=List[User])
async def read_users():
    return await user_service.get_users_from_supabase()

@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):
    return await user_service.create_user_in_supabase(user)
