from app.db.supabase_client import supabase_client
from app.models.user import User

async def get_users_from_supabase():
    response = supabase_client.table("users").select("*").execute()
    items_data = response.data
    return [User(**item_data) for item_data in items_data] # Convert each dict to Item model

async def create_user_in_supabase(user: User):
    user_dict = user.dict(exclude_none=True) # Convert Pydantic model to dict
    response = supabase_client.table("users").insert(user_dict).execute()
    created_item_data = response.data[0] # Assuming insert returns data
    return User(**created_item_data)
