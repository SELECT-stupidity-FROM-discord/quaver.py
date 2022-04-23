from typing import Tuple

import pkg_resources
import argparse
import platform
import aiohttp
import quaver
import sys

def show_version() -> None:
    entries = []

    entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
    version_info = quaver.version_info
    entries.append('- quaver.py v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(version_info))
    if version_info.releaselevel != 'final':
        pkg = pkg_resources.get_distribution('quaver.py')
        if pkg:
            entries.append(f'    - quaver.py pkg_resources: v{pkg.version}')

    entries.append(f'- aiohttp v{aiohttp.__version__}')
    uname = platform.uname()
    entries.append('- system info: {0.system} {0.release} {0.version}'.format(uname))
    print('\n'.join(entries))

def core(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    if args.version:
        show_version()
    else:
        parser.print_help()



def parse_args() -> Tuple[argparse.ArgumentParser, argparse.Namespace]:
    parser = argparse.ArgumentParser(prog='quaver', description='Tools for helping with quaver.py')
    parser.add_argument('-v', '--version', action='store_true', help='shows the library version')
    parser.set_defaults(func=core)
    return parser, parser.parse_args()


def main() -> None:
    parser, args = parse_args()
    args.func(parser, args)


if __name__ == '__main__':
    main()