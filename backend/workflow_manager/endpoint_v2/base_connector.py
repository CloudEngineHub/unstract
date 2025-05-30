import json
from typing import Any

from fsspec import AbstractFileSystem
from utils.constants import Common
from utils.user_context import UserContext

from unstract.connectors.filesystems import connectors
from unstract.connectors.filesystems.unstract_file_system import UnstractFileSystem
from unstract.workflow_execution.execution_file_handler import ExecutionFileHandler


class BaseConnector(ExecutionFileHandler):
    """Base class for connectors providing common methods and utilities."""

    def __init__(
        self,
        workflow_id: str,
        execution_id: str,
        organization_id: str,
        file_execution_id: str | None = None,
    ) -> None:
        """Initialize the BaseConnector class.

        This class serves as a base for connectors and provides common
        utilities.
        """
        super().__init__(workflow_id, execution_id, organization_id, file_execution_id)

    def get_fsspec(
        self, settings: dict[str, Any], connector_id: str
    ) -> AbstractFileSystem:
        """Get an fsspec file system based on the specified connector.

        Parameters:
        - settings (dict): Connector-specific settings.
        - connector_id (str): Identifier for the desired connector.

        Returns:
        AbstractFileSystem: An fsspec file system instance.

        Raises:
        KeyError: If the connector_id is not found in the connectors dictionary.
        """
        return self.get_fs_connector(
            settings=settings, connector_id=connector_id
        ).get_fsspec_fs()

    def get_fs_connector(
        self, settings: dict[str, Any], connector_id: str
    ) -> UnstractFileSystem:
        """Get an fs connector based specified connector settings.

        Parameters:
        - settings (dict): Connector-specific settings.
        - connector_id (str): Identifier for the desired connector.

        Returns:
        UnstractFileSystem: An unstract fs connector instance.
        """
        if connector_id not in connectors:
            raise ValueError(f"Connector '{connector_id}' is not supported.")
        connector = connectors[connector_id][Common.METADATA][Common.CONNECTOR]
        return connector(settings)

    @classmethod
    def get_json_schema(cls, file_path: str) -> dict[str, Any]:
        """Load and return a JSON schema from the specified file path.

        Parameters:
        - file_path (str): The path to the JSON schema file.

        Returns:
        dict: The loaded JSON schema.

        Raises:
        json.JSONDecodeError: If there is an issue decoding the JSON file.
        """
        try:
            with open(file_path, encoding="utf-8") as file:
                schema: dict[str, Any] = json.load(file)
        except OSError:
            schema = {}
        return schema

    @classmethod
    def get_api_storage_dir_path(cls, workflow_id: str, execution_id: str) -> str:
        """Get the directory path for storing api files.

        Parameters:
        - workflow_id (str): Identifier for the workflow.
        - execution_id (str): Identifier for the execution.
        - organization_id (Optional[str]): Identifier for the organization
            (default: None).

        Returns:
        str: The directory path for the execution.
        """
        organization_id = UserContext.get_organization_identifier()
        api_storage_dir: str = cls.get_api_execution_dir(
            workflow_id, execution_id, organization_id
        )
        return api_storage_dir

    @classmethod
    def get_execution_dir_path(cls, workflow_id: str, execution_id: str) -> str:
        """Get the directory path for storing execution-related files.

        Parameters:
        - workflow_id (str): Identifier for the workflow.
        - execution_id (str): Identifier for the execution.

        Returns:
        str: The directory path for the execution.
        """
        organization_id = UserContext.get_organization_identifier()
        execution_dir: str = cls.get_execution_dir(
            workflow_id, execution_id, organization_id
        )
        return execution_dir
