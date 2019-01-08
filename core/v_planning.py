# -*- coding: utf-8 -*-

from math import ceil, sqrt, hypot
import matplotlib.pyplot as plt


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
        Lest = V_cmd * Tstr
    else:
        Nc = ceil((length - L_min) / (f * sampling_time))
        Tc = Nc * sampling_time
        V_cmd = length / (Tstr + Tc)
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
    a = V_cmd / Tstr
    j = a / sampling_time
    s_tmp = []
    v_tmp = []
    acc_tmp = []
    for i in range(step3):

        t = i * sampling_time
        if i < step1:
            acc = a
            fed = acc * t
            pos = 0.5 * acc * t * t

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

    plt.plot(list(i * 0.001 for i in range(len(s_tmp))), s_tmp)
    plt.show()


def s_shape_interplation(ox, oy, x, y, f):

    length = hypot((x - ox), (y - oy))
    Nss = 0
    Nc = 0
    amax = Amax
    # need to define Jmax
    Jmax = 50000
    Lmin = 2 * f * sqrt(f / Jmax)
    Nstr = ceil((Lmin / 2 / Jmax / sampling_time ** 3) ** (1 / 3))
    Tstr = Nstr * sampling_time

    if length <= Lmin:
        Nstr = ceil((length / 2 / Jmax / sampling_time ** 3) ** (1 / 3))
        Tstr = Nstr * sampling_time
        Jmax = length / (2 * Tstr ** 3)
        amax = Jmax * Tstr
        Vcmd = amax * Tstr
    else:
        Tc = length / f - 2 * Tstr
        Nc = ceil(Tc / sampling_time)
        Tc = Nc * sampling_time
        Vcmd = length / (2 * Tstr + Tc)
        amax = Vcmd / Tstr
        Jmax = amax / Tstr

    step1 = Nstr
    step2 = step1 + Nstr
    step3 = step2 + Nc
    step4 = step3 + Nstr
    step5 = step4 + Nstr

    t0 = 0
    t1 = step1 * sampling_time
    t2 = step2 * sampling_time
    t3 = step3 * sampling_time
    t4 = step4 * sampling_time
    t5 = step5 * sampling_time

    s_tmp = []
    v_tmp = []
    acc_tmp = []
    jerk_tmp = []

    for j in range(step5):
        t = j * sampling_time
        if j < step1:
            jerk = Jmax
            acc = Jmax * (t - t0)
            fed = 0.5 * Jmax * (t - t0) ** 2
        elif step1 <= j < step2:
            jerk = -Jmax
            acc = Jmax * (t2 - t)
            fed = Vcmd - 0.5 * Jmax * (t2 - t) ** 2
        elif step2 <= j < step3:
            jerk = 0
            acc = 0
            fed = Vcmd
        elif step3 <= j < step4:
            jerk = -Jmax
            acc = -Jmax * (t - t3)
            fed = Vcmd - 0.5 * Jmax * (t - t3) ** 2
        elif j >= step4:
            jerk = Jmax
            acc = -Jmax * (t5 - t)
            fed = 0.5 * Jmax * (t5 - t) ** 2

        else:
            raise ValueError

        # s_tmp.append(pos)
        v_tmp.append(fed)
        acc_tmp.append(acc)
        jerk_tmp.append(jerk)

    return v_tmp, acc_tmp, jerk_tmp


if __name__ == '__main__':
    from nc import nc_reader
    with open("../line.nc") as textfile:
        text = textfile.read()
    v_plot = []
    a_plot = []
    j_plot = []
    for ox, oy, x, y, of in nc_reader(text):
        # interpolation_2d(ox, oy, x, y, of)
        v, a, j = s_shape_interplation(ox, oy, x, y, of)
        v_plot.extend(v)
        a_plot.extend(a)
        j_plot.extend(j)
    plt.plot(list(i * 0.001 for i in range(len(v_plot))), j_plot)
    plt.show()
