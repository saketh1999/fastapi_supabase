# app/services/item_service.py
from app.db.supabase_client import supabase_client
from app.models.item import Item

async def get_items_from_supabase():
    response = supabase_client.table("items").select("*").execute()
    items_data = response.data
    return [Item(**item_data) for item_data in items_data] # Convert each dict to Item model

async def create_item_in_supabase(item: Item):
    item_dict = item.dict(exclude_none=True) # Convert Pydantic model to dict
    response = supabase_client.table("items").insert(item_dict).execute()
    created_item_data = response.data[0] # Assuming insert returns data
    return Item(**created_item_data)
