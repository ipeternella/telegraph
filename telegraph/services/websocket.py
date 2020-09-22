from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


class WebSocketService:
    """
    Service responsible for dealing with web sockets connections and removals.
    """

    def __init__(self):
        self._websocket_pool: List[WebSocket] = []

    @property
    def web_socket_pool(self):
        return self._websocket_pool

    async def connect(self, websocket: WebSocket):
        """
        Accepts and appends a new web socket to the pool.
        """
        await websocket.accept()
        self._websocket_pool.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
        Removes a web socket from the pool.
        """
        self._websocket_pool.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """
        Sends a message to a specific web socket.
        """
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        """
        Broadcasts a message to all the web sockets in the pool.
        """
        for connection in self._web_socket_pool:
            await connection.send_text(message)
