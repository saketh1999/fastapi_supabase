# main.py
from fastapi import FastAPI
from app.api import items as items_router # Import the router from app/api/items.py
from app.api import users as users_router # Import the router from app/api/users.py

app = FastAPI(title="My Supabase FastAPI App")

app.include_router(items_router.router) # Include the item router

app.include_router(users_router.router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI with Supabase!"}
