# -*- coding: utf-8 -*-

import re


def match(patten: str, doc: str):
    yield from re.compile(patten).finditer(doc)


def nc_code_compiler(path: str):
    with open(path, encoding='utf-8') as f:
        nc_doc = f.read().upper()
    
    command = []
    for m in match(
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


def plot(
    v_cmd: float,
    a_max: float,
    j_max: float,
    t0: float,
    t: float,
    t1: float
):
    """Plot of s, v, a, j."""
    s = v_cmd * t
    v = v_cmd

    if t == t0:
        a = a_max
        j = j_max
    elif t == t1:
        a = -a_max
        j = -j_max
    else:
        a = 0
        j = 0

    return s, v, a, j
