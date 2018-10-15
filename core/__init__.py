# -*- coding: utf-8 -*-

from typing import Iterable, Any


def print_matrix(m: Iterable[Any]):
    """Print a numpy matrix."""
    for row in m:
        s = []
        for v in row:
            try:
                s.append(f"{v:.02f}")
            except (ValueError, TypeError):
                s.append(f"{v}")
        print(",\t".join(s))
