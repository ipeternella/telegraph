"""
Exceptions raised by the app.
"""


class MissingConfigurationException(BaseException):
    """
    Raised when a config is missing such as an env var.
    """
