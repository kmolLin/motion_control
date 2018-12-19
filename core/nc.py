# -*- coding: utf-8 -*-

from typing import (
    Iterator,
    Tuple,
    Match,
    AnyStr,
)
import re


def _match(patten: str, doc: str) -> Iterator[Match[AnyStr]]:
    yield from re.compile(patten).finditer(doc)


def _nc_compiler(path: str):
    with open(path, encoding='utf-8') as f:
        nc_doc = f.read().upper()

    command = []
    for m in _match(
        r"G(\d{1,2})\s"
        r"X([+-]?\d+\.?\d*)\s"
        r"Y([+-]?\d+\.?\d*)"
        r"(?:\sZ([+-]?\d+\.?\d*))?"
        r"(?:\sF(\d+\.?\d*))?",
        nc_doc
    ):
        g = int(m.group(1))
        x = float(m.group(2))
        y = float(m.group(3))
        if m.group(4):
            z = float(m.group(4))
        else:
            z = None
        if m.group(5):
            f = float(m.group(5)) / 60.
        else:
            f = None

        command.append((g, x, y, z, f))

    return command


def nc_reader(path: str) -> Iterator[Tuple[float, float, float, float, float]]:
    """Parser of NC code."""
    command = _nc_compiler(path)
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
