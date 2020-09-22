"""
Models of the application.
"""

# chat_room_distributed_connections
{
    "chat_room_id": "6576b56b-8c96-47d0-b17f-70ef3d84bfda",
    "max_connections": 6,
    "current_connections": 3,  # 1 connection on another server instnace
    "hosting_servers": [
        {
            "server_id": "4945c63c-0e8b-4fb2-810b-5c8071091e04",
            "users": [
                {
                    "user_id": "1c101959-b95e-4c08-bd69-a2e1ee759646",
                    "created_at": "2017-04-13T14:34:23.111142+00:00",
                },
                {
                    "user_id": "8e9404e6-ba38-4118-9a19-0060314be702",
                    "created_at": "2017-04-13T14:34:23.111142+00:00",
                },
            ],
        },
        {
            "server_id": "dad41fef-8445-4d96-8501-0deeed39cccb",
            "users": [
                {
                    "user_id": "b2491548-d1e2-41e1-9fbb-c0e2a4943d8b",
                    "created": "¿2017-04-13T14:34:23.111142+00:00",
                }
            ],
        },
    ],
}

# web_socket_connections
{
    "web_sockets_connections": [
        {
            "chat_room_id": "b2491548-d1e2-41e1-9fbb-c0e2a4943d8b",
            "users": [
                {"user_id": "1c101959-b95e-4c08-bd69-a2e1ee759646", "web_socket": ""},
                {"user_id": "8e9404e6-ba38-4118-9a19-0060314be702", "web_socket": ""},
            ],
        }
    ]
}

# chat_room
{
    "chat_room_id": "b2491548-d1e2-41e1-9fbb-c0e2a4943d8b",
    "name": "igp room",
    "max_connections": 6,
    "min_age": 20,
}

# chat_message
{
    "chat_room_id": "b2491548-d1e2-41e1-9fbb-c0e2a4943d8b",
    "user_id": "1c101959-b95e-4c08-bd69-a2e1ee759646",
    "message": "hello, world!",
}

# user
{
    "user_id": "1c101959-b95e-4c08-bd69-a2e1ee759646",
    "user_name": "igp",
    "age": 29,
}
