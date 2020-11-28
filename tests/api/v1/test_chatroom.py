"""
Tests for the v1 chatroom endpoints.
"""
import json
import uuid

from httpx import AsyncClient
from tortoise.contrib import test

from src.core.models.entities import ChatRoom
from src.settings import SERVER_FULL_BIND_ADDRESS
from src.startup import fastapi_server


class TestSomething(test.TestCase):
    async def test_something_async(self):
        """
        Should get all chatrooms.
        """
        # arrange
        endpoint = "api/v1/chatroom"
        chatroom_creation_data = {"name": f"test room {uuid.uuid4()}", "description": "hehe", "max_concurrent_users": 2}

        # act
        async with AsyncClient(app=fastapi_server, base_url=SERVER_FULL_BIND_ADDRESS) as client:
            response1 = await client.post(endpoint, data=json.dumps(chatroom_creation_data))

        chatrooms = await ChatRoom.all()

        # assert
        assert response1.status_code == 200
        assert len(chatrooms) == 1
