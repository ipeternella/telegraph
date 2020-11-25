"""
Module with routes regarding the Question entity.
"""
from fastapi import APIRouter

# from src.core.boundaries.schemas import QuestionQuerySetResponse
from src.core.boundaries.schemas import QuestionCreationRequest
from src.core.boundaries.schemas import QuestionResponse
from src.core.boundaries.schemas import QuestionsResponse
from src.core.services import questions as questions_service

questions_router = APIRouter()


@questions_router.get("/", response_model=QuestionsResponse)
async def get_all_questions(skip: int = 0, limit: int = 10):
    """
    Gets paginated questions from the database.
    """
    questions = await questions_service.get_questions(skip, limit)
    return questions


@questions_router.post("/", response_model=QuestionResponse)
async def create_new_question(question_creation_dto: QuestionCreationRequest):
    """
    Creates a new question about me.
    """
    created_question = await questions_service.create_question(question_creation_dto)
    return created_question
