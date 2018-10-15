# -*- coding: utf-8 -*-

from typing import Union
from numpy import array, ndarray, pi
from sympy import (
    Float,
    Expr,
    Symbol,
    sin,
    cos,
)
import yaml


def print_matrix(m: ndarray):
    """Print a numpy matrix."""
    for row in m:
        print(", ".join((f"{v:.02f}" if type(v) == Float else f"{v}") for v in row))


def transform(
    # h_t
    z_ht: Union[float, Expr] = Symbol('z_ht'),
    # b_h
    y_bh: Union[float, Expr] = Symbol('y_bh'),
    z_bh: Union[float, Expr] = Symbol('z_bh'),
    # z_b
    theta_b: Union[float, Expr] = Symbol('theta_b'),
    y_zb: Union[float, Expr] = Symbol('y_zb'),
    z_zb: Union[float, Expr] = Symbol('z_zb'),
    # f_z
    y_fz: Union[float, Expr] = Symbol('y_fz'),
    z_fz: Union[float, Expr] = Symbol('z_fz'),
    zm: Union[float, Expr] = Symbol('zm'),
    # y_f
    y_yf: Union[float, Expr] = Symbol('y_yf'),
    z_yf: Union[float, Expr] = Symbol('z_yf'),
    ym: Union[float, Expr] = Symbol('ym'),
    # x_y
    z_xy: Union[float, Expr] = Symbol('z_xy'),
    xm: Union[float, Expr] = Symbol('xm'),
    # c_x
    theta_c: Union[float, Expr] = Symbol('theta_c'),
    z_cx: Union[float, Expr] = Symbol('z_cx'),
    # w_c
    z_wc: Union[float, Expr] = Symbol('z_wc'),
    # r_w
    x_rw: Union[float, Expr] = Symbol('x_rw'),
    y_rw: Union[float, Expr] = Symbol('y_rw'),
    z_rw: Union[float, Expr] = Symbol('z_rw'),
    **_
) -> ndarray:
    """Forward transform function."""
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
        array(r_w)
        .dot(array(w_c))
        .dot(array(c_x))
        .dot(array(x_y))
        .dot(array(y_f))
        .dot(array(f_z))
        .dot(array(z_b))
        .dot(array(b_h))
        .dot(array(h_t))
    )


if __name__ == '__main__':
    # mechanism data
    with open("BZYXC_5_axis.yml", 'r') as f:
        data = yaml.load(f.read())

    r_t = transform(
        xm=82.250,
        ym=0,
        zm=-82.25,
        theta_b=pi / 2,
        theta_c=-pi / 2,
        **data
    )
    print_matrix(r_t)
