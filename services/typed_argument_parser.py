from tap import Tap


class TypedArgumentParser(Tap):
    """
    CPSC 4240 Malware Scanner
    It does stuff
    """
    directory_to_scan: str  # directory to scan

    def configure(self) -> None:
        self.add_argument('directory_to_scan')