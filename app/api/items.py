# app/api/items.py
from fastapi import APIRouter, Depends
from typing import List

from app.services import item_service
from app.models.item import Item

router = APIRouter()

@router.get("/items/", response_model=List[Item])
async def read_items():
    return await item_service.get_items_from_supabase()

@router.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    return await item_service.create_item_in_supabase(item)
