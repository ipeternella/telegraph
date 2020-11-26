"""
Models used by the chatting system.
"""
from tortoise import fields

from src.core.models.base import BaseEntityMixin


class User(BaseEntityMixin):
    """
    Models a chat user.
    """

    nick_name = fields.CharField(max_length=255, unique=True)


class ChatRoom(BaseEntityMixin):
    """
    Models a chat room.
    """

    name = fields.CharField(max_length=255, unique=True)
    description = fields.CharField(max_length=255)
    max_concurrent_users = fields.IntField()


class Message(BaseEntityMixin):
    """
    Models a chat message.
    """

    message = fields.CharField(max_length=255)

    chat_room: fields.ForeignKeyRelation[ChatRoom] = fields.ForeignKeyField("models.ChatRoom", related_name="messages")
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="messages")
