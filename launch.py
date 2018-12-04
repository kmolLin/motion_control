# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import yaml
from numpy import pi
from core.forward_kinematics import forward_transform
from core.inverse_kinematics import inverse_transform
from core.line_interpolation import line_interpolation_2d
from core.nc import nc_code_compiler, plot
from core import print_matrix


if __name__ == '__main__':
    command = nc_code_compiler("line.nc")
    ox = 0
    oy = 0
    for g, x, y, z, f in command:
        if f:
            v_cmd, a_max, j_max, t_c = line_interpolation_2d(ox, oy, x, y, f)
            plot_list = []
            for t in range(100 + 1):
                s, v, a, j = plot(v_cmd, a_max, j_max, 0, t_c * t / 100, t_c)
                plot_list.append(a)
            plt.plot(plot_list)
            plt.show()
        ox = x
        oy = y
