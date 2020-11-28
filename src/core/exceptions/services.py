"""
Exceptions raised by services
"""


class EntityAlreadyExists(Exception):
    """
    Raised when an entity already exists in the database and was not expected.
    """
