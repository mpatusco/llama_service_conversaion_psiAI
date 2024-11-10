"""FastAPI main application.

This file initializes the FastAPI application and includes routers for handling 
requests related to conversation management.

Attributes:
    app (FastAPI): The main FastAPI application instance.
"""

from fastapi import FastAPI
from app.api.v1 import conversation_routes

app = FastAPI()

app.include_router(conversation_routes.router, prefix="/api/v1/conversation")
