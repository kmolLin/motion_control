# -*- coding: utf-8 -*-

from typing import Union
from numpy import (
    array,
    ndarray,
    float16 as np_float16,
)
from sympy import (
    Expr,
    Symbol,
    sin,
    cos,
)


def forward_transform(
    xm: float,
    ym: float,
    zm: float,
    theta_b: float,
    theta_c: float,

    # h_t
    z_ht: Union[float, Expr] = Symbol('z_ht'),
    # b_h
    y_bh: Union[float, Expr] = Symbol('y_bh'),
    z_bh: Union[float, Expr] = Symbol('z_bh'),
    # z_b
    y_zb: Union[float, Expr] = Symbol('y_zb'),
    z_zb: Union[float, Expr] = Symbol('z_zb'),
    # f_z
    y_fz: Union[float, Expr] = Symbol('y_fz'),
    z_fz: Union[float, Expr] = Symbol('z_fz'),
    # y_f
    y_yf: Union[float, Expr] = Symbol('y_yf'),
    z_yf: Union[float, Expr] = Symbol('z_yf'),
    # x_y
    z_xy: Union[float, Expr] = Symbol('z_xy'),
    # c_x
    z_cx: Union[float, Expr] = Symbol('z_cx'),
    # w_c
    z_wc: Union[float, Expr] = Symbol('z_wc'),
    # r_w
    x_rw: Union[float, Expr] = Symbol('x_rw'),
    y_rw: Union[float, Expr] = Symbol('y_rw'),
    z_rw: Union[float, Expr] = Symbol('z_rw'),
    **_
) -> ndarray:
    """Forward forward_transform function."""
    h_t = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -z_ht],
        [0, 0, 0, 1],
    ]

    b_h = [
        [1, 0, 0, 0],
        [0, 1, 0, -y_bh],
        [0, 0, 1, -z_bh],
        [0, 0, 0, 1],
    ]

    z_b = [
        [cos(theta_b), 0, sin(theta_b), 0],
        [0, 1, 0, -y_zb],
        [-sin(theta_b), 0, cos(theta_b), -z_zb],
        [0, 0, 0, 1],
    ]

    f_z = [
        [1, 0, 0, 0],
        [0, 1, 0, y_fz],
        [0, 0, 1, z_fz + zm],
        [0, 0, 0, 1],
    ]

    y_f = [
        [1, 0, 0, 0],
        [0, 1, 0, y_yf + ym],
        [0, 0, 1, -z_yf],
        [0, 0, 0, 1],
    ]

    x_y = [
        [1, 0, 0, xm],
        [0, 1, 0, 0],
        [0, 0, 1, -z_xy],
        [0, 0, 0, 1],
    ]

    c_x = [
        [cos(theta_c), sin(theta_c), 0, 0],
        [-sin(theta_c), cos(theta_c), 0, 0],
        [0, 0, 1, -z_cx],
        [0, 0, 0, 1],
    ]

    w_c = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -z_wc],
        [0, 0, 0, 1],
    ]

    r_w = [
        [1, 0, 0, x_rw],
        [0, 1, 0, y_rw],
        [0, 0, 1, -z_rw],
        [0, 0, 0, 1],
    ]

    return (
        array(r_w, dtype=np_float16)
        .dot(array(w_c, dtype=np_float16))
        .dot(array(c_x, dtype=np_float16))
        .dot(array(x_y, dtype=np_float16))
        .dot(array(y_f, dtype=np_float16))
        .dot(array(f_z, dtype=np_float16))
        .dot(array(z_b, dtype=np_float16))
        .dot(array(b_h, dtype=np_float16))
        .dot(array(h_t, dtype=np_float16))
    )
