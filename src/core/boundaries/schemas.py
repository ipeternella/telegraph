"""
Schemas used for some DTOs.
"""
from src.core.boundaries.base_schemas import ChatRoomBaseMixin
from src.core.boundaries.base_schemas import EntityFromDatabaseMixin


class ChatRoomCreationRequest(ChatRoomBaseMixin):
    """
    Chat room creation DTO.
    """

    pass


class ChatRoomResponse(EntityFromDatabaseMixin, ChatRoomBaseMixin):
    """
    Chat room response DTO.
    """

    class Config:
        orm_mode = True
