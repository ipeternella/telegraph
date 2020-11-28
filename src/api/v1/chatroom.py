"""
Module with routes regarding the Chat Room entity.
"""
from typing import List

from fastapi import APIRouter
from pydantic.types import UUID4

from src.core.boundaries.base_schemas import LimitOffsetPaginationResult
from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.boundaries.schemas import ChatRoomResponse
from src.core.services import chatroom_service

chatroom_router = APIRouter()


@chatroom_router.get("/{chatroom_id}", response_model=ChatRoomResponse)
async def get_chatroom_by_id(chatroom_id: UUID4):
    """
    Gets paginated chat rooms from the database.
    """
    chatroom = await chatroom_service.get_chatroom_by_id(chatroom_id)

    return chatroom


@chatroom_router.get("/", response_model=LimitOffsetPaginationResult[List[ChatRoomResponse]])
async def get_chatrooms(offset: int = 0, limit: int = 10):
    """
    Gets paginated chat rooms from the database.
    """
    paginated_chatrooms, total = await chatroom_service.get_chatrooms(offset, limit)
    return LimitOffsetPaginationResult(results=paginated_chatrooms, total=total, limit=limit, offset=offset)


@chatroom_router.post("/", response_model=ChatRoomResponse)
async def create_chatroom(chatroom_creation_request: ChatRoomCreationRequest):
    """
    Creates a new chat room.
    """
    created_chatroom = await chatroom_service.create_chatroom(chatroom_creation_request)

    return created_chatroom
