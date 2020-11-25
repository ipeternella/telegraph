from fastapi import FastAPI
from tortoise.contrib.starlette import register_tortoise

from src.api.v1.questions import questions_router
from src.settings import TORTOISE_ORM


def create_server() -> FastAPI:
    """
    Creates and setups the main FastAPI-based server.
    """
    # app server
    server = FastAPI()

    # routes
    server.include_router(questions_router, prefix="/api/v1/questions")

    # db
    register_tortoise(server, config=TORTOISE_ORM)

    return server
