from pathlib import Path
from typing import Union
import pandas as pd
import config


class DatabaseReader:
    @staticmethod
    def read_database(path: Union[Path, str]):
        db = pd.read_csv(path, comment='#')
        db.set_index(config.MALWARE_DB_INDEX_NAME, inplace=True)
        return db
