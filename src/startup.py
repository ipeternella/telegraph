"""
Startup code for the FastAPI server: creates a new server instance and sets it up for usage.
"""

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from tortoise.contrib.starlette import register_tortoise
from tortoise.exceptions import DoesNotExist

from src.api.v1.chatroom import chatroom_router
from src.core.exceptions.services import EntityAlreadyExists
from src.settings import TORTOISE_ORM


def _setup_exception_handlers(fastapi_server: FastAPI) -> None:
    """
    Adds customized exception handlers to the server.
    """

    @fastapi_server.exception_handler(DoesNotExist)
    async def does_not_exist_handler(req: Request, exc: DoesNotExist):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @fastapi_server.exception_handler(EntityAlreadyExists)
    async def entity_already_exists_handler(req: Request, exc: EntityAlreadyExists):
        return JSONResponse(status_code=422, content={"detail": str(exc)})


def _setup_routes(fastapi_server: FastAPI) -> None:
    """
    Setups the server routes.
    """
    fastapi_server.include_router(chatroom_router, prefix="/api/v1/chatroom")


def _setup_databases(fastapi_server: FastAPI) -> None:
    """
    Setups databases used by the server.
    """
    register_tortoise(fastapi_server, config=TORTOISE_ORM)


def create_fastapi_server() -> FastAPI:
    """
    Creates and setups the main FastAPI-based server.
    """
    fastapi_server = FastAPI()

    _setup_routes(fastapi_server)
    _setup_exception_handlers(fastapi_server)
    _setup_databases(fastapi_server)

    return fastapi_server


fastapi_server = create_fastapi_server()
