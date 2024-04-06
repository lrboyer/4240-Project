from pathlib import Path
from typing import Union
import pandas as pd


class DatabaseReader:
    @staticmethod
    def read_database(path: Union[Path, str]):
        db = pd.read_csv(path, comment='#')
        db.set_index("sha256_hash", inplace=True)
        return db
