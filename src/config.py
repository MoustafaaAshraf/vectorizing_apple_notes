from typing import Dict, Any
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# value = os.getenv("APPLE_NOTES_DB_PATH")
# print(value)


def get_env_variable(var_name: str, default: Any = None, required: bool = False) -> Any:
    """
    Get an environment variable or return a default value

    :param var_name: Name of the environment variable
    :param default: Default value if the environment variable is not set
    :param required: If True, raise an error when the variable is not set
    :return: Value of the environment variable or the default value
    """
    value = os.getenv(var_name)
    if value is None:
        if required:
            raise ValueError(
                f"Environment variable '{var_name}' is required but not set."
            )
        return default
    return value


# Configuration dictionary
CONFIG: Dict[str, Any] = {
    "db_path": get_env_variable(
        "APPLE_NOTES_DB_PATH",
        default=str(
            Path.home()
            / "Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"
        ),
        required=False,
    ),
    "vector_model": get_env_variable(
        "VECTOR_MODEL", default="sentence-transformers/all-MiniLM-L6-v2", required=False
    ),
    "index_file": get_env_variable(
        "INDEX_FILE", default="apple_notes_vectors.index", required=False
    ),
    "max_vector_size": int(
        get_env_variable("MAX_VECTOR_SIZE", default=1000, required=False)
    ),
    "preprocessing_steps": get_env_variable(
        "PREPROCESSING_STEPS",
        default="remove_html,lowercase,remove_punctuation",
        required=False,
    ).split(","),
}


# Validate configuration
def validate_config(config: Dict[str, Any]) -> None:
    """
    Validate the configuration dictionary

    :param config: Configuration dictionary to validate
    :raises ValueError: If any validation fails
    """
    if not os.path.exists(config["db_path"]):
        raise ValueError(f"Database file not found at {config['db_path']}")

    if config["max_vector_size"] <= 0:
        raise ValueError("MAX_VECTOR_SIZE must be a positive integer")


# Run validation
validate_config(CONFIG)
