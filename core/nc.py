# -*- coding: utf-8 -*-

from typing import (
    Iterator,
    Tuple,
    Match,
    AnyStr,
)
import re


DEFAULT_NC_SYNTAX = (
    r"(?:G(\d{1,2})\s)?"
    r"X([+-]?\d+\.?\d*)\s"
    r"Y([+-]?\d+\.?\d*)"
    r"(?:\sZ([+-]?\d+\.?\d*))?"
    r"(?:\sF(\d+\.?\d*))?"
)


def _match(patten: str, doc: str) -> Iterator[Match[AnyStr]]:
    yield from re.compile(patten.encode('utf-8')).finditer(doc.encode('utf-8'))


def _nc_compiler(nc_doc: str, syntax: str):
    command = []
    for m in _match(syntax, nc_doc):
        if m.group(1) is not None:
            g = int(m.group(1))
        else:
            g = 1
        x = float(m.group(2))
        y = float(m.group(3))
        if m.group(4) is not None:
            z = float(m.group(4))
        else:
            z = None
        if m.group(5) is not None:
            f = float(m.group(5)) / 60.
        else:
            f = None
        command.append((g, x, y, z, f))

    return command


def nc_reader(
    nc_doc: str,
    syntax: str = DEFAULT_NC_SYNTAX
) -> Iterator[Tuple[float, float, float, float, float]]:
    """Parser of NC code."""
    command = _nc_compiler(nc_doc, syntax)
    ox = 0.
    oy = 0.
    of = None
    for g, x, y, z, f in command:
        if of is None:
            if f is None:
                raise ValueError("no feed rate setting")
            of = f
        if ox == x and oy == y:
            continue

        yield ox, oy, x, y, of

        ox = x
        oy = y
        if f is not None:
            of = f
