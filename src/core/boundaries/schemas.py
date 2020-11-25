"""
Schemas used for some DTOs.
"""
from typing import List

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.pydantic.creator import pydantic_queryset_creator

from src.core.boundaries.base_schemas import AnswerBaseMixin
from src.core.boundaries.base_schemas import QuestionBaseMixin
from src.core.models.entities import Answer
from src.core.models.entities import Question


class AnswerCreationRequest(AnswerBaseMixin):
    """
    Answer creation DTO.
    """


class QuestionCreationRequest(QuestionBaseMixin):
    """
    Question creation DTO.
    """


QuestionResponse = pydantic_model_creator(Question)
# QuestionQuerySetResponse = pydantic_queryset_creator(Question)

AnswerResponse = pydantic_model_creator(Answer)


class QuestionsResponse(QuestionBaseMixin):
    answers: List[QuestionResponse]
