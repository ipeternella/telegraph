"""
Base schemas reused by some DTOs.
"""
from datetime import datetime
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class ApiResponse(GenericModel, Generic[T]):
    """
    Basic API response schema.

    Examples:
    {
        "results": {"hello": "world"},
        "errors: null
    }
    {
        "results": null,
        "errors: ["Something went wrong!"]
    }
    """

    results: Optional[T]
    errors: Optional[List[str]]


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
