"""
Main settings of the telegraph's project.
"""
import os
from typing import List

from src.infra.env import getenv_as_list
from src.infra.env import getenv_or_exception

# project settings
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# server settings
SERVER_BIND_ADDRESS = getenv_or_exception("SERVER_BIND_ADDRESS")
SERVER_BIND_PORT = int(getenv_or_exception("SERVER_BIND_PORT"))
SERVER_FULL_BIND_ADDRESS = f"http://{SERVER_BIND_ADDRESS}:{SERVER_BIND_PORT}"

# cors
ALLOWED_HOSTS: List[str] = getenv_as_list("ALLOWED_HOSTS", default_value="*")
ALLOWED_HEADERS = getenv_as_list("ALLOWED_HEADERS", default_value="*")
ALLOWED_METHODS = getenv_as_list("ALLOWED_METHODS", default_value="*")

# databases
DATABASE_CONNECTION_URI = getenv_or_exception("DATABASE_CONNECTION_URI")
TORTOISE_ORM = {
    "connections": {"default": DATABASE_CONNECTION_URI},
    "apps": {
        "models": {
            "models": ["src.core.models.entities", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
