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

    async def test_should_assert_pagination_works_properly(self):
        """
        Should make a request to api/v1/chatroom and pagination must work accordingly.
        """
        # arrange
        await ChatRoom.create(name="igu room 1", description="description 1", max_concurrent_users=2)
        await ChatRoom.create(name="igu room 2", description="description 2", max_concurrent_users=4)
        await ChatRoom.create(name="igu room 3", description="description 3", max_concurrent_users=6)

        # act
        pagination_params_1 = {
            "offset": 1,
            "limit": 2,
        }  # skips igu room 1

        pagination_params_2 = {
            "offset": 2,
            "limit": 10,
        }  # skips igu room 1 + igu room 2

        pagination_params_with_name_filter = {
            "offset": 0,
            "limit": 5,
            "name": "igu room 2",
        }  # there can be no offset, or no results would be returned

        async with AsyncClient(app=fastapi_server, base_url=self.TEST_CLIENT_BASE_URL) as client:
            paginated_response_1 = await client.get(self.CHATROOM_ENDPOINT_V1, params=pagination_params_1)
            paginated_response_2 = await client.get(self.CHATROOM_ENDPOINT_V1, params=pagination_params_2)
            paginated_response_filter_by_name = await client.get(
                self.CHATROOM_ENDPOINT_V1, params=pagination_params_with_name_filter
            )

        # assert - paginated_response_1
        paginated_response_1_body = paginated_response_1.json()
        paginated_response_2_body = paginated_response_2.json()

        assert paginated_response_1.status_code == 200
        assert paginated_response_2.status_code == 200

        assert paginated_response_1_body["total"] == 3
        assert paginated_response_1_body["limit"] == 2
        assert paginated_response_1_body["offset"] == 1

        assert len(paginated_response_1_body["results"]) == 2
        assert paginated_response_1_body["results"][0]["name"] == "igu room 2"
        assert paginated_response_1_body["results"][1]["name"] == "igu room 3"

        # assert - paginated_response_2
        paginated_response_2_body = paginated_response_2.json()
        assert paginated_response_2.status_code == 200

        assert paginated_response_2_body["total"] == 3
        assert paginated_response_2_body["limit"] == 10
        assert paginated_response_2_body["offset"] == 2

        assert len(paginated_response_2_body["results"]) == 1
        assert paginated_response_2_body["results"][0]["name"] == "igu room 3"

        # assert - paginated_response_filter_by_name
        paginated_response_filter_by_name_body = paginated_response_filter_by_name.json()

        assert paginated_response_filter_by_name.status_code == 200
        assert paginated_response_filter_by_name_body["total"] == 1
        assert paginated_response_filter_by_name_body["limit"] == 5
        assert paginated_response_filter_by_name_body["offset"] == 0

        assert len(paginated_response_filter_by_name_body["results"]) == 1
        assert paginated_response_filter_by_name_body["results"][0]["name"] == "igu room 2"
