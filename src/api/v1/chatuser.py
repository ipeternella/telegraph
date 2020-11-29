"""
Module with routes regarding the User entity.
"""
from typing import List
from typing import Optional

from fastapi import APIRouter
from pydantic.types import UUID4

from src.core.boundaries.base_schemas import LimitOffsetPaginationResult
from src.core.boundaries.schemas import ChatUserCreationRequest
from src.core.boundaries.schemas import ChatUserResponse
from src.core.services import chatuser_service

chatuser_router = APIRouter()


@chatuser_router.get("/{chatuser_id}", response_model=ChatUserResponse)
async def get_chatuser_by_id(chatuser_id: UUID4):
    """
    Gets a chat user by its id.
    """
    user = await chatuser_service.get_user_by_id(chatuser_id)

    return user


@chatuser_router.get("/", response_model=LimitOffsetPaginationResult[List[ChatUserResponse]])
async def get_chatusers(offset: int = 0, limit: int = 10, nick_name: Optional[str] = None):
    """
    Gets paginated chat users from the database.
    """
    paginated_users, total = await chatuser_service.get_users(offset, limit, nick_name)

    return LimitOffsetPaginationResult(results=paginated_users, total=total, limit=limit, offset=offset)


@chatuser_router.post("/", response_model=ChatUserResponse)
async def create_user(user_creation_request: ChatUserCreationRequest):
    """
    Creates a new user.
    """
    created_user = await chatuser_service.create_user(user_creation_request)

    return created_user
