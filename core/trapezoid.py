# -*- coding: utf-8 -*-

from typing import (
    Tuple,
    Callable,
    Iterator,
    Type,
    TypeVar,
)
from abc import abstractmethod
from math import (
    ceil,
    sqrt,
    hypot,
    sin,
    cos,
    atan2,
)
from .nc import nc_reader, DEFAULT_NC_SYNTAX


class StepTimeError(ValueError):

    def __init__(self, t: float, t_str: float, t_end: float):
        super(StepTimeError, self).__init__(
            f"time {t} is not in the range ({t_str:.04f} ~ {t_end:.04f})"
        )


_T_back = TypeVar('_T_back')


class Velocity:

    __slots__ = ('length', 'c_from', 'c_to', 'angle', 's_base', 't')

    t_s = 1e-3

    @abstractmethod
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        t0: float,
        s_base: float
    ):
        self.c_from = (x1, y1)
        self.c_to = (x2, y2)
        self.angle = atan2(y2 - y1, x2 - x1)
        self.length = hypot(x2 - x1, y2 - y1)
        self.s_base = s_base
        self.t = [t0]

    @abstractmethod
    def a(self, t: float) -> float:
        ...

    @abstractmethod
    def v(self, t: float) -> float:
        ...

    @abstractmethod
    def s(self, t: float) -> float:
        ...

    def a_xy(self, t: float) -> Tuple[float, float]:
        a = self.a(t)
        return (a * cos(self.angle)), (a * sin(self.angle))

    def v_xy(self, t: float) -> Tuple[float, float]:
        v = self.v(t)
        return (v * cos(self.angle)), (v * sin(self.angle))

    def s_xy(self, t: float) -> Tuple[float, float]:
        s = self.s(t) - self.s_base
        bx, by = self.c_from
        return (bx + s * cos(self.angle)), (by + s * sin(self.angle))

    def iter(self, *funcs: Callable[[float], _T_back]) -> Iterator[Tuple[_T_back, ...]]:
        for i in range(int((self.t[-1] - self.t[0]) / self.t_s) + 1):
            yield tuple(func(self.t[0] + i * self.t_s) for func in funcs)


class Trapezoid(Velocity):

    __slots__ = (
        'c_from', 'c_to', 'length', 'angle',
        'case', 't_c', 't_str',
        '__l1', '__l2',
        's_base', 't',
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
        t0: float = 0.,
        s_base: float = 0.
    ):
        super(Trapezoid, self).__init__(x1, y1, x2, y2, t0, s_base)
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
        self.t.append(self.t[0] + s1 * self.t_s)
        self.t.append(self.t[0] + s2 * self.t_s)
        self.t.append(self.t[0] + s3 * self.t_s)

        self.v_max = v_cmd
        self.a_max = v_cmd / t_str
        self.j_max = self.a_max / self.t_s

    def a(self, t: float) -> float:
        if t == self.t[0]:
            return 0.
        elif self.t[0] < t <= self.t[1]:
            return self.a_max
        elif self.t[1] < t <= self.t[2]:
            return 0.
        elif self.t[2] < t < self.t[3]:
            return -self.a_max
        elif t == self.t[3]:
            return 0.

        raise StepTimeError(t, self.t[0], self.t[3])

    def v(self, t: float) -> float:
        if self.t[0] <= t < self.t[1]:
            return self.a_max * (t - self.t[0])
        elif self.t[1] <= t <= self.t[2]:
            return self.v_max
        elif self.t[2] < t <= self.t[3]:
            return self.a_max * (self.t[3] - t)

        raise StepTimeError(t, self.t[0], self.t[3])

    def s(self, t: float) -> float:
        if self.t[0] <= t < self.t[1]:
            dt = t - self.t[0]
            return self.s_base + 0.5 * self.a_max * dt * dt
        elif self.t[1] <= t <= self.t[2]:
            return self.s_base + self.__l1 + self.v_max * (t - self.t[1])
        elif self.t[2] < t <= self.t[3]:
            dt = self.t[3] - t
            return self.s_base + self.__l2 - 0.5 * self.a_max * dt * dt

        raise StepTimeError(t, self.t[0], self.t[3])


def graph_chart(
    nc_doc: str,
    syntax: str = DEFAULT_NC_SYNTAX,
    strategy: Type[Velocity] = Trapezoid
) -> Iterator[Velocity]:
    """Chart data.

    Usage:

    s_plot: List[Tuple[float]] = []
    for tp in graph_chart(nc_doc, syntax, strategy):
        sxy_plot.extend(tp.iter(tp.s))

    sxy_plot: List[Tuple[float, float]] = []
    for tp in graph_chart(nc_doc, syntax, strategy):
        sxy_plot.extend(tp.iter(tp.s_xy))
    """
    bs = 0.
    for ox, oy, x, y, of in nc_reader(nc_doc, syntax):
        # X axis: [i * tp.t_s for i in range(len(plot))]
        tp = strategy(ox, oy, x, y, of, s_base=bs)
        yield tp
        bs = tp.s(tp.t[-1])
