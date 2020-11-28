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


class ChatroomApiV1Tests(test.TestCase):
    """
    Chatroom-related v1 api integration tests.
    """

    async def test_should_create_and_get_all_chatrooms(self):
        """
        Should create a chatroom with api/v1/chatroom call and assert final database state.
        """

        # arrange
        endpoint = "api/v1/chatroom"
        chatroom_creation_data = {
            "name": f"test room {uuid.uuid4()}",
            "description": "something",
            "max_concurrent_users": 2,
        }

        # act
        async with AsyncClient(app=fastapi_server, base_url=SERVER_FULL_BIND_ADDRESS) as client:
            creation_response = await client.post(endpoint, data=json.dumps(chatroom_creation_data))

        all_db_chatrooms = await ChatRoom.all()
        creation_response_body = creation_response.json()

        # assert -- http response
        assert creation_response.status_code == 200
        assert creation_response_body["name"] == chatroom_creation_data["name"]
        assert creation_response_body["description"] == chatroom_creation_data["description"]
        assert creation_response_body["max_concurrent_users"] == chatroom_creation_data["max_concurrent_users"]

        # assert - db state
        assert len(all_db_chatrooms) == 1
