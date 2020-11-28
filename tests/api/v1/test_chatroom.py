"""
Tests for the v1 chatroom endpoints.
"""
import json

from httpx import AsyncClient
from tortoise.contrib import test

from src.core.models.entities import ChatRoom
from src.settings import SERVER_FULL_BIND_ADDRESS
from src.startup import fastapi_server


class ChatroomApiV1Tests(test.TestCase):
    """
    Chatroom-related v1 api integration tests.
    """

    CHATROOM_ENDPOINT_V1 = "api/v1/chatroom"
    TEST_CLIENT_BASE_URL = SERVER_FULL_BIND_ADDRESS

    async def test_should_create_and_get_all_chatrooms(self):
        """
        Should create a chatroom with api/v1/chatroom call and assert final database state.
        """
        # arrange
        chatroom_creation_data = {
            "name": "test room one",
            "description": "test",
            "max_concurrent_users": 2,
        }

        # act
        async with AsyncClient(app=fastapi_server, base_url=self.TEST_CLIENT_BASE_URL) as client:
            creation_response = await client.post(self.CHATROOM_ENDPOINT_V1, data=json.dumps(chatroom_creation_data))

        # assert -- http response
        all_db_chatrooms = await ChatRoom.all()
        creation_response_body = creation_response.json()

        assert creation_response.status_code == 200
        assert creation_response_body["name"] == chatroom_creation_data["name"]
        assert creation_response_body["description"] == chatroom_creation_data["description"]
        assert creation_response_body["max_concurrent_users"] == chatroom_creation_data["max_concurrent_users"]

        # assert - db state
        assert len(all_db_chatrooms) == 1

    async def test_should_create_one_room_and_not_another_with_same_name(self):
        """
        Should create a chatroom with api/v1/chatroom call and reject subsequent creation of
        rooms with the same name.
        """
        # arrange
        chatroom_creation_data = {
            "name": "test room one",
            "description": "test",
            "max_concurrent_users": 2,
        }

        repeated_chatroom_creation_data = {
            "name": "test room one",
            "description": "test repeat",
            "max_concurrent_users": 4,
        }

        # act
        async with AsyncClient(app=fastapi_server, base_url=self.TEST_CLIENT_BASE_URL) as client:
            creation_response = await client.post(self.CHATROOM_ENDPOINT_V1, data=json.dumps(chatroom_creation_data))
            repeated_creation_response = await client.post(
                self.CHATROOM_ENDPOINT_V1, data=json.dumps(repeated_chatroom_creation_data)
            )

        # assert -- http response
        all_db_chatrooms = await ChatRoom.all()
        repeated_creation_response_body = repeated_creation_response.json()

        assert creation_response.status_code == 200
        assert repeated_creation_response.status_code == 422
        assert repeated_creation_response_body["detail"] == "Chatroom name is already taken."

        # assert - db state
        assert len(all_db_chatrooms) == 1
