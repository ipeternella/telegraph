"""
Module with routes regarding the Chat Room entity.
"""
from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from pydantic.types import UUID4
from tortoise.exceptions import DoesNotExist

from src.core.boundaries.base_schemas import ApiResponse
from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.boundaries.schemas import ChatRoomResponse
from src.core.exceptions.services import EntityAlreadyExists
from src.core.services import chatroom_service

chatroom_router = APIRouter()


@chatroom_router.get("/{chatroom_id}", response_model=ChatRoomResponse)
async def get_chatroom_by_id(chatroom_id: UUID4):
    """
    Gets paginated chat rooms from the database.
    """
    try:
        chatroom = await chatroom_service.get_chatroom_by_id(chatroom_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Chatroom was not found.")

    return chatroom


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
    try:
        created_chatroom = await chatroom_service.create_chatroom(chatroom_creation_request)
    except EntityAlreadyExists:
        raise HTTPException(status_code=422, detail="Chatroom name is already taken.")

    return created_chatroom
