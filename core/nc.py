# -*- coding: utf-8 -*-

import re


def match(patten: str, doc: str):
    yield from re.compile(patten).finditer(doc)


def nc_code_compiler(path: str):
    with open(path, encoding='utf-8') as f:
        nc_doc = f.read().upper()
    
    command = []
    for m in match(r"G(\d{1,2})\sX([+-]?\d+\.?\d*)\sY([+-]?\d+\.?\d*)", nc_doc):
        command.append((
            int(m.group(1)),
            float(m.group(2)),
            float(m.group(3)),
        ))
    print(command)
