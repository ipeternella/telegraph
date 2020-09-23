"""
Settings used to setup the application.
"""
from telegraph.infra.env import getenv_or_exception

DATABASE = {"connection": getenv_or_exception("DATABASE_CONNECTION_STRING")}
