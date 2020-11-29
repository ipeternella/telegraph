"""
Chatroom-related service.
"""
from typing import List
from typing import Optional
from typing import Tuple
from uuid import UUID

from tortoise.exceptions import DoesNotExist
from tortoise.queryset import QuerySet

from src.core.boundaries.schemas import ChatRoomCreationRequest
from src.core.exceptions.services import EntityAlreadyExists
from src.core.models.entities import ChatRoom


async def get_chatrooms(offset: int = 0, limit: int = 10, name: Optional[str] = None) -> Tuple[List[ChatRoom], int]:
    """
    Gets a paginated slice of chatrooms from the database.
    """
    if name is not None:
        chatroom_queryset = ChatRoom.filter(name=name)
    else:
        chatroom_queryset = ChatRoom.all()

    paginated_chatrooms = await chatroom_queryset.offset(offset).limit(limit)
    total = await chatroom_queryset.count()

    return paginated_chatrooms, total


async def get_chatroom_by_id(id: UUID) -> ChatRoom:
    """
    Get a specific chatroom
    """
    try:
        return await ChatRoom.get(id=id)
    except DoesNotExist as e:
        raise DoesNotExist("Chatroom was not found.") from e


async def create_chatroom(chatroom_creation_request: ChatRoomCreationRequest) -> ChatRoom:
    """
    Creates a new chatroom resource in the database.
    """
    if await ChatRoom.filter(name=chatroom_creation_request.name, is_active=True).exists():
        raise EntityAlreadyExists("Chatroom name is already taken.")

    created_chatroom = await ChatRoom.create(
        name=chatroom_creation_request.name,
        description=chatroom_creation_request.description,
        max_concurrent_users=chatroom_creation_request.max_concurrent_users,
    )

    return created_chatroom
