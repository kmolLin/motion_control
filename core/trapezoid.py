# -*- coding: utf-8 -*-

from typing import Tuple
from abc import abstractmethod
from math import (
    ceil,
    sqrt,
    hypot,
    sin,
    cos,
    atan2,
)
from matplotlib import pyplot
from .nc import nc_reader


class StepTimeError(ValueError):

    def __init__(self, t: float, t_str: float, t_end: float):
        super(StepTimeError, self).__init__(
            f"time {t} is not in the range ({t_str:.04f} ~ {t_end:.04f})"
        )


class Velocity:

    __slots__ = ('length', 'c_from', 'c_to', 'angle')

    t_s = 1e-3

    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float
    ):
        self.c_from = (x1, y1)
        self.c_to = (x2, y2)
        self.angle = atan2(y2 - y1, x2 - x1)
        self.length = hypot(x2 - x1, y2 - y1)

    @abstractmethod
    def a(self, t: float) -> float:
        ...

    @abstractmethod
    def v(self, t: float) -> float:
        ...

    @abstractmethod
    def s(self, t: float, s_base: float = 0.) -> float:
        ...

    def a_xy(self, t: float) -> Tuple[float, float]:
        a = self.a(t)
        return (a * cos(self.angle)), (a * sin(self.angle))

    def v_xy(self, t: float) -> Tuple[float, float]:
        v = self.v(t)
        return (v * cos(self.angle)), (v * sin(self.angle))

    def s_xy(self, t: float) -> Tuple[float, float]:
        s = self.s(t)
        bx, by = self.c_from
        return (bx + s * cos(self.angle)), (by + s * sin(self.angle))


class Trapezoid(Velocity):

    __slots__ = (
        'c_from', 'c_to', 'length', 'angle',
        'case', 't_c', 't_str',
        '__l1', '__l2',
        't0', 't1', 't2', 't3',
        'v_max', 'a_max', 'j_max',
    )

    __a_max = 2500

    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        feed_rate: float,
        t0: float = 0.
    ):
        super(Trapezoid, self).__init__(x1, y1, x2, y2)
        n_c = 0
        n_str = ceil(feed_rate / (self.__a_max * self.t_s))
        t_str = n_str * self.t_s
        l_min = feed_rate * t_str

        if self.length <= l_min:
            self.case = 0
            n_str = ceil(sqrt(self.length / (self.__a_max * self.t_s * self.t_s)))
            t_str = n_str * self.t_s
            t_c = 0
            v_cmd = self.length / t_str
            # l_est = v_cmd * t_str
        else:
            self.case = 1
            n_c = ceil((self.length - l_min) / (feed_rate * self.t_s))
            t_c = n_c * self.t_s
            v_cmd = self.length / (t_str + t_c)
            # l_est = v_cmd * (t_str + t_c)

        self.t_c = t_c
        self.t_str = t_str

        self.__l1 = 0.5 * v_cmd * t_str
        self.__l2 = v_cmd * (t_str + t_c)

        s1 = n_str
        s2 = s1 + n_c
        s3 = s2 + n_str
        self.t0 = t0
        self.t1 = t0 + s1 * self.t_s
        self.t2 = t0 + s2 * self.t_s
        self.t3 = t0 + s3 * self.t_s

        self.v_max = v_cmd
        self.a_max = v_cmd / t_str
        self.j_max = self.a_max / self.t_s

    def a(self, t: float) -> float:
        if t == self.t0:
            return 0.
        elif self.t0 < t <= self.t1:
            return self.a_max
        elif self.t1 < t <= self.t2:
            return 0.
        elif self.t2 < t < self.t3:
            return -self.a_max
        elif t == self.t3:
            return 0.

        raise StepTimeError(t, self.t0, self.t3)

    def v(self, t: float) -> float:
        if self.t0 <= t < self.t1:
            return self.a_max * (t - self.t0)
        elif self.t1 <= t <= self.t2:
            return self.v_max
        elif self.t2 < t <= self.t3:
            return self.a_max * (self.t3 - t)

        raise StepTimeError(t, self.t0, self.t3)

    def s(self, t: float, s_base: float = 0.) -> float:
        if self.t0 <= t < self.t1:
            dt = t - self.t0
            return s_base + 0.5 * self.a_max * dt * dt
        elif self.t1 <= t <= self.t2:
            return s_base + self.__l1 + self.v_max * (t - self.t1)
        elif self.t2 < t <= self.t3:
            dt = self.t3 - t
            return s_base + self.__l2 - 0.5 * self.a_max * dt * dt

        raise StepTimeError(t, self.t0, self.t3)


def graph_chart(nc_doc: str):
    bs = 0.
    sx_plot = []
    sy_plot = []
    s_plot = []
    v_plot = []
    a_plot = []
    for ox, oy, x, y, of in nc_reader(nc_doc):
        tp = Trapezoid(ox, oy, x, y, of)
        for i in range(int(tp.t3 / tp.t_s) + 1):
            st = i * tp.t_s
            rx, ry = tp.s_xy(st)
            sx_plot.append(rx)
            sy_plot.append(ry)
            s_plot.append(tp.s(st, bs))
            v_plot.append(tp.v(st))
            a_plot.append(tp.a(st))
        bs = s_plot[-1]

    pyplot.plot(list(i * 0.001 for i in range(len(sy_plot))), sy_plot)
    pyplot.show()
