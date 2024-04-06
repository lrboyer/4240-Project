import os
from typing import Union
from pathlib import Path


def list_files_in_directory(directory: Union[Path, str]):
    """
    @return: list of all files in directory
    """
    return [
        os.path.join(root, filename)
        for root, directories, files in os.walk(directory)
        for filename in files
    ]