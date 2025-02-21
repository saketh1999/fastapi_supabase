# app/middleware/not_found_middleware.py
from fastapi import Request, Response
from starlette.status import HTTP_404_NOT_FOUND

async def not_found_middleware(request: Request, call_next):
    """
    Middleware to return a custom "Sorry, wrong query" response for unmatched endpoints.
    """
    try:
        response = await call_next(request) # First, let the request proceed down the chain
    except Exception: # Catch any exceptions that might occur down the line. Not strictly needed for "Not Found" but good practice for robust middleware.
        raise # Re-raise the exception if you want standard error handling

    if response.status_code == HTTP_404_NOT_FOUND: # Check if the response is already a 404 (Not Found)
        return Response(
            content="Sorry, wrong query",
            status_code=HTTP_404_NOT_FOUND,
            media_type="text/plain" # or "application/json" if you prefer JSON response
        )
    return response # If it's not a 404, return the original response