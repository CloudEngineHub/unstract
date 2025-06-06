from typing import Any


class ConnectorBaseException(Exception):
    """Base class for exceptions from Unstract connectors."""

    def __init__(
        self, *args: Any, user_message: str | None = None, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self._user_message = user_message

    @property
    def user_message(self) -> str | None:
        return self._user_message


class ConnectorError(ConnectorBaseException):
    """Exceptions related to connectors."""

    def __init__(
        self,
        message: str,
        *args: Any,
        treat_as_user_message: bool = False,
        **kwargs: Any,
    ) -> None:
        user_message = message if treat_as_user_message else None
        super().__init__(*args, user_message=user_message, **kwargs)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"


class FSAccessDeniedError(ConnectorError):
    """Handles all FS access denied error.

    Args:
        ConnectorError: Inherits from base ConnectorError class
    """


class AzureHttpError(ConnectorError):
    """Handles invalid directory error from azure.

    Args:
        ConnectorError (Class): Inherits class ConnectorError
    """


class PermissionDeniedError(ConnectorError):
    """Handles permission denied error from fs connector.

    Args:
        ConnectorError (Class): Inherits class ConnectorError
    """


class FileHashNotFound(ConnectorError):
    """Handles file hash not found error from fs connector.

    Args:
        ConnectorError (Class): Inherits class ConnectorError
    """
