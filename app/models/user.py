from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None  # Assuming your Supabase table has an 'id' primary key, could be UUID too
    name: str
    description: str | None = None
    age: int | None = None
