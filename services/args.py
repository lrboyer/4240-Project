import typed_argparse as tap


class Args(tap.TypedArgs):
    directory_to_scan: str = tap.arg(positional=True, help='directory to scan')
