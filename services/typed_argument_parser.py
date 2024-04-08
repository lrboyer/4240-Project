from tap import Tap
from typing import Literal


class TypedArgumentParser(Tap):
    """
    CPSC 4240 Malware Scanner
    """
    action: Literal['scan', 'watch', 'lock', 'unlock']
    filepath: str  # path to file

    verbose: bool = False  # print more detail
    quarantine: str = '.'  # directory to move quarantined files

    def configure(self) -> None:
        self.add_argument('action')
        self.add_argument('filepath')
        self.add_argument('-v', '--verbose')
        self.add_argument('-q', '--quarantine')
