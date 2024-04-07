from pathlib import Path
from typing import Union
from cryptography.fernet import Fernet
import shutil


class FilePrison:
    """
    Quarantine File
    """
    def __init__(self, key: str, destination: Union[Path, str] = '.'):
        """
        :param destination: the location where quarantined file will end up

        """
        self.fernet = Fernet(key)
        self.destination = destination

    def lock_file(self, file: Union[Path, str]):
        with open(file, 'rb') as f:
            data = f.read()
        with open(file, 'wb') as f:
            encrypted_data = self.fernet.encrypt(data)
            f.write(encrypted_data)

    def unlock_file(self, file: Union[Path, str]):
        with open(file, 'rb') as f:
            data = f.read()
        with open(file, 'wb') as f:
            decrypted_data = self.fernet.decrypt(data)
            f.write(decrypted_data)

    def quarantine(self, file: Union[Path, str]):
        """
        disarm file and move it to the destination
        """
        self.lock_file(file)
        shutil.move(file, self.destination)

