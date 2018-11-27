# -*- coding: utf-8 -*-

import re


def match(patten: str, doc: str):
    yield from re.compile(patten).finditer(doc)


def nc_code_compiler(path: str):
    with open(path, encoding='utf-8') as f:
        nc_doc = f.read().upper()
    
    command = []
    for m in match(r"G(\d{1,2})\sX([+-]?\d+\.?\d*)\sY([+-]?\d+\.?\d*)(?:\sF(\d+\.?\d*))?", nc_doc):
        g = int(m.group(1))
        x = float(m.group(2))
        y = float(m.group(3))
        try:
            f = float(m.group(4))
        except TypeError:
            command.append((g, x, y))
        else:
            command.append((g, x, y, f))
    print(command)
