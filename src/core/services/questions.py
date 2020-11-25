"""
Services regarding Questions entities.
"""
from typing import List

from src.core.boundaries.schemas import QuestionCreationRequest
from src.core.models.entities import Answer
from src.core.models.entities import Question


async def get_questions(skip: int = 0, limit: int = 10) -> List[Question]:
    """
    Gets paginated questions set.
    """
    questions = await Question.all().offset(skip).limit(limit).prefetch_related("answers")

    return questions


async def create_question(question_creation_dto: QuestionCreationRequest):
    """
    Creates a new question about me.
    """
    question = await Question.create(question=question_creation_dto.question, is_active=question_creation_dto.is_active)
    await Answer.create(answer="Fine, thanks!", is_active=True, question=question)

    return question
