from fastapi import FastAPI
from tortoise.contrib.starlette import register_tortoise

from src.api.v1.chatroom import chatroom_router
from src.settings import TORTOISE_ORM


def create_server() -> FastAPI:
    """
    Creates and setups the main FastAPI-based server.
    """
    # app server
    server = FastAPI()

    # routes
    server.include_router(chatroom_router, prefix="/api/v1/chatroom")

    # db
    register_tortoise(server, config=TORTOISE_ORM)

    return server
