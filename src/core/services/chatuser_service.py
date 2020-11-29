"""
User-related service.
"""
from typing import List
from typing import Optional
from typing import Tuple

from pydantic.types import UUID4
from tortoise.exceptions import DoesNotExist

from src.core.boundaries.schemas import ChatUserCreationRequest
from src.core.exceptions.services import EntityAlreadyExists
from src.core.models.entities import ChatUser


async def get_users(offset: int = 0, limit: int = 10, nick_name: Optional[str] = None) -> Tuple[List[ChatUser], int]:
    """
    Gets a paginated slice of chat users from the database.
    """
    if nick_name is not None:
        users_queryset = ChatUser.filter(nick_name=nick_name)
    else:
        users_queryset = ChatUser.all()

    paginated_users = await users_queryset.offset(offset).limit(limit)
    total = await users_queryset.count()

    return paginated_users, total


async def get_user_by_id(id: UUID4) -> ChatUser:
    """
    Get a specific chat user.
    """
    try:
        return await ChatUser.get(id=id)
    except DoesNotExist as e:
        raise DoesNotExist("Chat user was not found.") from e


async def create_user(user_creation_request: ChatUserCreationRequest) -> ChatUser:
    """
    Creates a new chat user resource in the database.
    """
    if await ChatUser.filter(nick_name=user_creation_request.nick_name).exists():
        raise EntityAlreadyExists("User nick_name is already taken.")

    created_chatuser = await ChatUser.create(
        first_name=user_creation_request.first_name,
        last_name=user_creation_request.last_name,
        age=user_creation_request.age,
        nick_name=user_creation_request.nick_name,
    )

    return created_chatuser
