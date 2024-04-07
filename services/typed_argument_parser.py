from tap import Tap
from typing import Optional


class TypedArgumentParser(Tap):
    """
    CPSC 4240 Malware Scanner
    It does stuff
    """
    directory_to_scan: str  # directory to scan
    verbose: bool = False

    def configure(self) -> None:
        self.add_argument('directory_to_scan')
        self.add_argument('-v', '--verbose')
