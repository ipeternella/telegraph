"""
Schemas used for some DTOs.
"""
from src.core.boundaries.base_schemas import ChatRoomBaseMixin
from src.core.boundaries.base_schemas import ChatUserBaseMixin
from src.core.boundaries.base_schemas import EntityFromDatabaseMixin


class ChatRoomCreationRequest(ChatRoomBaseMixin):
    """
    Chatroom creation DTO.
    """

    pass


class ChatUserCreationRequest(ChatUserBaseMixin):
    """
    User creation DTO.
    """

    pass


class ChatRoomResponse(EntityFromDatabaseMixin, ChatRoomBaseMixin):
    """
    Chatroom response DTO.
    """

    class Config:
        orm_mode = True  # response will be an object, not a dict


class ChatUserResponse(EntityFromDatabaseMixin, ChatUserBaseMixin):
    """
    User response DTO.
    """

    class Config:
        orm_mode = True  # response will be an object, not a dict
