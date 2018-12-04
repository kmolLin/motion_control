# -*- coding: utf-8 -*-

from math import (
    degrees,
    hypot,
    ceil,
    atan2,
)


def line_interpolation_2d(
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    feed_rate: float,
    t_s: float = 1e-3
):
    """Line interpolation."""
    delta_x = x1 - x0
    delta_y = y1 - y0
    theta = atan2(delta_y, delta_x)
    l_tcp = hypot(delta_x, delta_y)

    t_c = feed_rate / l_tcp

    n_c = ceil(l_tcp / (feed_rate * t_s))
    v_cmd = l_tcp / (n_c * t_s)
    a_max = v_cmd / t_s
    j_max = a_max / t_s
    return v_cmd, a_max, j_max, t_c


def trapezoid_2d(
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    feed_rate: float,
    t_s: float = 1e-3
):
    """Trapezoid ACC/DEC"""
    # TODO: Trapezoid ACC/DEC
