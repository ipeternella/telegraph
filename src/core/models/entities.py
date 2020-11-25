"""
Models used by the application.
"""
from tortoise import fields

from src.core.models.base import BaseEntityMixin


class Question(BaseEntityMixin):
    """
    Models a question that might be asked to the fox bot.
    """

    question = fields.CharField(max_length=255)
    is_active = fields.BooleanField()

    answers: fields.ReverseRelation["Answer"]


class Answer(BaseEntityMixin):
    """
    Models an answer that might be returned by the fox bot.
    """

    answer = fields.CharField(max_length=255)
    is_active = fields.BooleanField()

    question: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField("models.Question", related_name="answers")
