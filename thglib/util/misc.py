from __future__ import division

import base64
import errno
import os
import re
import signal
import six
import socket
import stat
import string
import subprocess
import sys
import tempfile

from thglib.util.constante import (
    KB,
    MB,
    GB,
    KiB,
    MiB,
    GiB,

)


def align(alignment: object, x) -> int:
    """align(alignment, x) -> int
    Rounds `x` up to nearest multiple of the `alignment`.
    Example:
      >>> [align(5, n) for n in range(15)]
      [0, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15]
    """
    return x + -x % alignment


def align_down(alignment, x):
    """align_down(alignment, x) -> int
    Rounds `x` down to nearest multiple of the `alignment`.
    Example:
        >>> [align_down(5, n) for n in range(15)]
        [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10]
    """
    return x - x % alignment


def binary_to_ip(host):
    """binary_ip(host) -> str
    Resolve host and return IP as four byte string.
    Example:
        >>> binary_to_ip("127.0.0.1")
        b'\\x7f\\x00\\x00\\x01'
    """
    return socket.inet_aton(socket.gethostbyname(host))


def size(n, abbrev='B', si=False):
    """size(n, abbrev = 'B', si = False) -> str
    Convert the length of a bytestream to human readable frm.

    """
    if hasattr(n, '__len__'):
        n = len(n)

    base = 1000.0 if si else 1024.0
    if n < base:
        return '%d%s' % (n, abbrev)

    for suffix in ['K', 'M', 'G', 'T']:
        n /= base
        if n < base:
            return '%.02f%s%s' % (n, suffix, abbrev)

    return '%.02fP%s' % (n / base, abbrev)

def read(path,count=-1,skip=0)->str:
    """

    Args:
        path: -> str
        count: -> int
        skip: - int

    Returns: -> byte_string
     >>> read('/proc/self/exe')[:4]
        b'\x7fELF'

    """
