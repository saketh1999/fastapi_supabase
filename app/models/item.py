# app/models/item.py
from pydantic import BaseModel

class Item(BaseModel):
    id: int | None = None  # Assuming your Supabase table has an 'id' primary key, could be UUID too
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
