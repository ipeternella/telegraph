"""
Models used by the chatting system.
"""
from tortoise import fields

from src.core.models.base import BaseEntityMixin


class ChatUser(BaseEntityMixin):
    """
    Models a chat user.
    """

    # personal data
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    age = fields.SmallIntField()

    # app data
    nick_name = fields.CharField(max_length=255, unique=True)


class ChatRoom(BaseEntityMixin):
    """
    Models a chatroom.
    """

    name = fields.CharField(max_length=255, index=True)
    description = fields.CharField(max_length=255)
    max_concurrent_users = fields.IntField()

    # after a while, rooms without any messages become inactive and are eligible to be recreated
    is_active = fields.BooleanField(default=True)

    class Meta:
        indexes = (("name", "is_active"),)


class ChatMessage(BaseEntityMixin):
    """
    Models a chat message coming from a user in a chatroom.
    """

    message = fields.CharField(max_length=255)

    chat_room: fields.ForeignKeyRelation[ChatRoom] = fields.ForeignKeyField("models.ChatRoom", related_name="messages")
    chat_user: fields.ForeignKeyRelation[ChatUser] = fields.ForeignKeyField("models.ChatUser", related_name="messages")
