# -*- coding: utf-8 -*-
# test_v_planning_with_trapezoid
from core.trapezoid import graph_chart
from core.controller_design import control_num_den, model_system
import matplotlib.pyplot as plt


if __name__ == '__main__':
    a = 1
    b = 200
    zeta = 0.707
    wn = 1000

    with open("./line.nc", "r") as f:
        doc = f.read()
    sx_plot, sy_plot, s_plot, v_plot, a_plot = graph_chart(doc)
    num, den = model_system(a, b, zeta, wn)
    for i in range(100):
        v_plot.append(0)
    smaple_time = 1e-3

    tout, yout = control_num_den(num, den, smaple_time, v_plot)
    plt.plot(tout, yout)
    plt.plot(tout, v_plot)
    plt.show()
    # toutx, sx = control_num_den(num, den, smaple_time, sx_plot)
    # touty, sy = control_num_den(num, den, smaple_time, sy_plot)
    # plt.plot(sx, sy)
    # plt.plot(sx_plot, sy_plot)
    # plt.show()

