"""
Entrypoint of the application which starts the server.
"""
import uvicorn

from src.settings import SERVER_BIND_ADDRESS
from src.settings import SERVER_BIND_PORT
from src.startup import create_server

server = create_server()

if __name__ == "__main__":
    uvicorn.run(server, host=SERVER_BIND_ADDRESS, port=SERVER_BIND_PORT)
