# -*- coding: utf-8 -*-

from core.nc import nc_code_compiler
from math import ceil, sqrt, hypot
import matplotlib.pyplot as plt
import numpy as np


sampling_time = 0.001
Amax = 2500


def interpolation_2d(ox, oy, x, y, f):

    length = hypot((x - ox), (y - oy))
    Nc = 0
    amax = Amax
    N_start = ceil(f / (amax * sampling_time))
    Tstr = N_start * sampling_time
    L_min = f * Tstr

    Lsblk = 0.0
    Nss = 0.0

    if length <= L_min:
        N_start = ceil(sqrt(length / (amax * sampling_time * sampling_time)))
        Tstr = N_start * sampling_time
        Tc = Nc * sampling_time
        V_cmd = length / Tstr
        A_max = V_cmd / Tstr
        Lest = V_cmd * Tstr

    else:
        Nc = ceil((length - L_min) / (f * sampling_time))
        Tc = Nc * sampling_time
        V_cmd = length / (Tstr + Tc)
        A_max = V_cmd / Tstr
        Lest = V_cmd * (Tstr + Tc)

    L1 = 0.5 * V_cmd * Tstr
    L2 = V_cmd * (Tstr + Tc)
    step1 = N_start
    step2 = step1 + Nc
    step3 = step2 + N_start
    t0 = 0
    t1 = step1 * sampling_time
    t2 = step2 * sampling_time
    t3 = step3 * sampling_time

    f = V_cmd
    a = A_max
    j = A_max / sampling_time
    s_tmp = []
    v_tmp = []
    acc_tmp = []
    for i in range(step3):

        t = i * sampling_time
        if i < step1:
            acc = a
            fed = acc * t
            pos = 0.5 * acc * t * t
        # print(i)

        elif step1 <= i <= step2:
            acc = 0
            fed = f
            pos = L1 + fed * (t - t1)

        else:
            acc = -a
            fed = a * (t3 - t)
            pos = L2 - 0.5 * a * (t3 - t) * (t3 - t)

        s_tmp.append(pos)
        v_tmp.append(fed)
        acc_tmp.append(acc)

    times = np.arange(0, len(s_tmp))
    plt.plot(times * 0.001, s_tmp)
    plt.show()


if __name__ == '__main__':
    command = nc_code_compiler("D:/kmol/motion_control/line.nc")
    ox = 0
    oy = 0
    for g, x, y, z, f in command:
        if f:
            interpolation_2d(ox, oy, x, y, f)

        ox = x
        oy = y




