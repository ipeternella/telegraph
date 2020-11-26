"""
Base schemas reused by some DTOs.
"""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class EntityFromDatabaseMixin(BaseModel):
    """
    Common properties shared by all entities from the database.
    """

    id: UUID
    created_at: datetime
    updated_at: datetime


class ChatRoomBaseMixin(BaseModel):
    """
    Common properties for ChatRoom entities.
    """

    name: str = Field(max_length=255)
    description: str = Field(max_length=255)
    max_concurrent_users: int
