from typing import NamedTuple, Literal

from .errors import *
from .quaver import *
from .enums import *


__title__ = 'quaver'
__author__ = 'SELECT-stupidity-FROM-discord'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present SELECT-stupidity-FROM-discord'
__version__ = '0.2.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=2, micro=0, releaselevel='candidate', serial=0)


del NamedTuple, Literal, VersionInfo