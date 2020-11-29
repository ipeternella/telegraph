"""
Base schemas reused by some DTOs.
"""
from datetime import datetime
from typing import Generic
from typing import Optional
from typing import TypeVar
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from pydantic.generics import GenericModel

T = TypeVar("T")


class LimitOffsetPaginationResult(GenericModel, Generic[T]):
    """
    Basic API response schema.

    Examples:
    {
        "results": [
            {"name": 3},  # skipped 2 results due to offset=2
            {"name": 4},
            {"name": 5},
            {"name": 6},
            {"name": 7},
        ],  # 5 results due to limit=5
        "total": 10,
        "offset": 2,
        "limit": 5,
    }
    """

    total: int
    limit: int
    offset: int
    results: Optional[T]


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
    def name_alphanumeric(cls, name: str):
        name_with_fixed_whitespaces = " ".join(name.split())
        name_without_whitespaces = "".join(name.split())

        assert name_without_whitespaces.isalnum(), "Chatroom name must contain only letters, numbers and spaces."
        return name_with_fixed_whitespaces


class ChatUserBaseMixin(BaseModel):
    """
    Common properties for User entities.
    """

    # personal data
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    age: int = Field(ge=16, le=120)  # 16 <= age <= 120

    # app data
    nick_name: str = Field(max_length=255)

    @validator("first_name", "last_name")
    def first_and_last_name_validation(cls, name: str):
        name_with_fixed_whitespaces = " ".join(name.split())
        name_without_whitespaces = "".join(name.split())

        assert name_without_whitespaces.isalpha(), "First and last names must contain only letters and spaces."
        return name_with_fixed_whitespaces
