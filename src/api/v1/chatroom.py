"""
Module with routes regarding the Chat Room entity.
"""
from typing import List

from fastapi import APIRouter

from src.core.boundaries.base_schemas import ApiResponse
from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.boundaries.schemas import ChatRoomResponse
from src.core.services import chatroom_service

chatroom_router = APIRouter()


@chatroom_router.get("/", response_model=ApiResponse[List[ChatRoomResponse]])
async def get_chatrooms(skip: int = 0, limit: int = 10):
    """
    Gets paginated chat rooms from the database.
    """
    chatrooms = await chatroom_service.get_chatrooms(skip, limit)
    return ApiResponse(results=chatrooms)


@chatroom_router.post("/", response_model=ChatRoomResponse)
async def create_chatroom(chatroom_creation_request: ChatRoomCreationRequest):
    """
    Creates a new chat room.
    """
    created_chatroom = await chatroom_service.create_chatroom(chatroom_creation_request)
    return created_chatroom
