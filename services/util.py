import os
import hashlib
import sys
from typing import Union
from pathlib import Path


def list_files_in_directory(directory: Union[Path, str]):
    """
    :return: list of all files in directory
    """
    return [
        os.path.join(root, filename)
        for root, directories, files in os.walk(directory)
        for filename in files
    ]


def hash_file(file_name: str):
    try:
        if not (os.path.isfile(file_name)):
            return
        with open(file_name, 'rb') as f:
            file_name_read = f.read()
            file_hash = hashlib.sha256(file_name_read).hexdigest()
            return file_hash

    except Exception as e:
        print(e, file=sys.stderr)