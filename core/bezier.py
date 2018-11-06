# -*- coding: utf-8 -*-

from typing import Tuple
from math import factorial


def bezier_formula(t, points) -> Tuple[float, float]:
    """Calculate coordinate of a point in the bezier curve"""
    n = len(points) - 1
    ox = oy = 0
    for i, (x, y) in enumerate(points):
        b = (t ** i) * ((1 - t) ** (n - i)) * factorial(n) / (factorial(i) * factorial(n - i))
        ox += x * b
        oy += y * b
    return ox, oy


def bezier_insert(t, points) -> Tuple[float, float]:
    if len(points) == 1:
        return points[0]

    tmp_list = []
    for i in range(len(points)):
        if i == len(points) - 1:
            break
        x, y = points[i]
        nx, ny = points[i + 1]
        tmp_list.append(((nx - x) * t + x, (ny - y) * t + y))

    return bezier_insert(t, tmp_list)


if __name__ == '__main__':
    print(bezier_insert(0.5, [
        (0, 0),
        (-100, 100),
        (100, 100),
        (0, 0),
    ]))
