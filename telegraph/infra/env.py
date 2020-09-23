"""
Environment variables related functions.
"""
import ast
import os
from typing import Any

from telegraph.exceptions.exceptions import MissingConfigurationException


def env2bool(env_var_name: str, default_var_value: Any) -> bool:
    """
    Evals env var strings as booleans. Accepts a default value.
    """
    env_var = os.getenv(env_var_name)

    if env_var is None:
        return default_var_value

    return ast.literal_eval(env_var)


def getenv_or_exception(env_name: str) -> str:
    """
    Gets an env variable or raises an exception.
    """
    if (env_value := os.getenv(env_name)) is None:
        raise MissingConfigurationException(
            "Missing required env var is missing: %s", env_name
        )

    return env_value
