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


class QuestionBaseMixin(BaseModel):
    """
    Common properties for Question entities.
    """

    question: str = Field(max_length=255)
    is_active: bool


class AnswerBaseMixin(BaseModel):
    """
    Common properties for Answer entities.
    """

    answer: str = Field(max_length=255)
    is_active: bool
