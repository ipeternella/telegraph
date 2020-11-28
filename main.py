"""
Entrypoint of the application which starts the server.
"""
import uvicorn

from src.settings import SERVER_BIND_ADDRESS
from src.settings import SERVER_BIND_PORT
from src.startup import fastapi_server

if __name__ == "__main__":
    uvicorn.run(fastapi_server, host=SERVER_BIND_ADDRESS, port=SERVER_BIND_PORT)
