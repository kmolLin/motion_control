# -*- coding: utf-8 -*-

from typing import Union

from typing import Tuple
from sympy import (
    Expr,
    Symbol,
    acos,
    atan2,
    cos,
    sin,
    atan,
)


def inverse_transform(
    q_x: float,
    q_y: float,
    q_z: float,
    k_x: float,
    k_y: float,
    k_z: float,

    # h_t
    z_ht: Union[float, Expr] = Symbol('z_ht'),
    # b_h
    z_bh: Union[float, Expr] = Symbol('z_bh'),
    # z_b
    z_zb: Union[float, Expr] = Symbol('z_zb'),
    z_fz: Union[float, Expr] = Symbol('z_fz'),
    z_xy: Union[float, Expr] = Symbol('z_xy'),
    z_wc: Union[float, Expr] = Symbol('z_wc'),
    # r_w
    x_rw: Union[float, Expr] = Symbol('x_rw'),
    y_rw: Union[float, Expr] = Symbol('y_rw'),
    z_rw: Union[float, Expr] = Symbol('z_rw'),
    z_yf: Union[float, Expr] = Symbol('z_xf'),
    z_cx: Union[float, Expr] = Symbol('z_cx'),
    **_
) -> Tuple[float, float, float, float, float]:
    """Parameters

    q_x: position x
    q_y: position y
    q_z: position z

    k_x: vector of x
    k_y: vector of y
    k_z: vector of z
    """
    z_bt = z_bh + z_ht
    z_rb = -z_rw - z_wc - z_cx - z_xy - z_yf + z_fz - z_zb
    theta_b = acos(k_z)
    if k_y == 0.and k_x == 0.:
        theta_c = atan(0.)
    else:
        theta_c = atan2(-k_y, k_x)
    x_m = cos(theta_c) * (q_x - x_rw) - sin(theta_c) * (q_y - y_rw) + sin(theta_b) * z_bt
    y_m = cos(theta_c) * (q_x - x_rw) + cos(theta_c) * (q_y - y_rw)
    z_m = q_z + cos(theta_b) * z_bt - z_rb

    return x_m, y_m, z_m, theta_b, theta_c
