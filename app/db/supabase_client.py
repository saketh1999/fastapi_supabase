# app/db/supabase_client.py
from supabase import create_client, Client
from app.core.config import settings

def get_supabase_client() -> Client:
    supabase_url: str = settings.supabase_url
    supabase_anon_key: str = settings.supabase_anon_key
    return create_client(supabase_url, supabase_anon_key)

supabase_client = get_supabase_client() # Initialize client - you can also use dependency injection later
