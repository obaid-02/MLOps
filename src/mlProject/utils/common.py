import os
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from omegaconf import OmegaConf  # Replaced ConfigBox with OmegaConf
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> OmegaConf:
    """Reads YAML file and returns an OmegaConf object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: if YAML file is empty.
        e: Any other exceptions.

    Returns:
        OmegaConf: OmegaConf object containing YAML data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return OmegaConf.create(content)  # Using OmegaConf.create() here
    except yaml.YAMLError:
        raise ValueError("YAML file is empty or invalid")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of directories to create.
        verbose (bool, optional): Whether to log the creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> OmegaConf:
    """Load data from a JSON file into an OmegaConf object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        OmegaConf: Configuration object with loaded data.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return OmegaConf.create(content)  # Using OmegaConf.create() here


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data to a binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
