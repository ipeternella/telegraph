"""
Schemas used for some DTOs.
"""
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.pydantic.creator import pydantic_queryset_creator

from src.core.boundaries.base_schemas import ChatRoomBaseMixin
from src.core.models.entities import ChatRoom


class ChatRoomCreationRequest(ChatRoomBaseMixin):
    """
    Chat room creation DTO.
    """

    name: str
    description: str
    max_concurrent_users: int


ChatRoomResponse = pydantic_model_creator(ChatRoom)
ChatRoomQuerySetResponse = pydantic_queryset_creator(ChatRoom)
