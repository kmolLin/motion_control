# -*- coding: utf-8 -*-

from typing import Iterable, Any


def print_matrix(m: Iterable[Any]):
    """Print a numpy matrix."""
    for i in range(4):
        if i == 3:
            print('-' * 45)
        s = []
        for j in range(4):
            v = m[i][j]
            try:
                s.append(f"{v:10.02f}")
            except (ValueError, TypeError):
                s.append(f"{v}")
            if j == 3:
                s[-1] = f"| {s[-1]}"
        print("".join(s))
