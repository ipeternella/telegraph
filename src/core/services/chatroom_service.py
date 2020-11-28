"""
Chatroom-related service.
"""
from typing import List

from fastapi.exceptions import HTTPException

from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.models.entities import ChatRoom


async def get_chatrooms(skip: int = 0, limit: int = 10) -> List[ChatRoom]:
    """
    Gets a paginated slice of chatrooms from the database.
    """
    chatrooms = await ChatRoom.all().offset(skip).limit(limit)

    return chatrooms


async def create_chatroom(chatroom_creation_request: ChatRoomCreationRequest) -> ChatRoom:
    """
    Creates a new chatroom resource in the database.
    """
    if await ChatRoom.filter(name=chatroom_creation_request.name, is_active=True).exists():
        raise HTTPException(status_code=422, detail="This chatroom name is already taken.")

    created_chatroom = await ChatRoom.create(
        name=chatroom_creation_request.name,
        description=chatroom_creation_request.description,
        max_concurrent_users=chatroom_creation_request.max_concurrent_users,
    )

    return created_chatroom
