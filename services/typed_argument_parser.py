from tap import Tap
from typing import Literal


class TypedArgumentParser(Tap):
    """
    CPSC 4240 Malware Scanner
    """
    action: Literal['scan', 'watch', 'lock', 'unlock']
    path: str  # directory to scan

    verbose: bool = False  # print more detail

    def configure(self) -> None:
        self.add_argument('action')
        self.add_argument('path')
        self.add_argument('-v', '--verbose')
