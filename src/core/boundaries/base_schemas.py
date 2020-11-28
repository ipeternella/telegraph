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
from pydantic import validator
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

    @validator("name")
    def username_alphanumeric(cls, name: str):
        name_with_fixed_whitespaces = " ".join(name.split())
        name_without_whitespaces = "".join(name.split())

        assert name_without_whitespaces.isalnum(), "Chatroom name must contain only letters, numbers and spaces."
        return name_with_fixed_whitespaces
