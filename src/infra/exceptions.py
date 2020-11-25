"""
Infra-related exceptions.
"""


class MissingEnvironmentVariable(Exception):
    """
    Raised when a required env var was not found.
    """
