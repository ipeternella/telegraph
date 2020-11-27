"""
Module with routes regarding the Chat Room entity.
"""
from typing import List

from fastapi import APIRouter

from src.core.boundaries.base_schemas import ApiResponse
from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.boundaries.schemas import ChatRoomResponse
from src.core.models.entities import ChatRoom

chatroom_router = APIRouter()


@chatroom_router.get("/", response_model=ApiResponse[List[ChatRoomResponse]])
async def get_chatrooms(skip: int = 0, limit: int = 10):
    """
    Gets paginated chat rooms from the database.
    """
    chatrooms = await ChatRoom.all().offset(skip).limit(limit)
    return ApiResponse(results=chatrooms)


@chatroom_router.post("/", response_model=ChatRoomResponse)
async def create_chatroom(chat_room_creation: ChatRoomCreationRequest):
    """
    Creates a new chat room.
    """
    created_chatroom = await ChatRoom.create(
        name=chat_room_creation.name,
        description=chat_room_creation.description,
        max_concurrent_users=chat_room_creation.max_concurrent_users,
    )

    return created_chatroom
