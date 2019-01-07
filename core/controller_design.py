# -*- coding: utf-8 -*-

from scipy.signal import dlsim, cont2discrete
import numpy as np
import matplotlib.pyplot as plt


def control_num_den(num, den, smapleing_time, input_data):
    # tf = TransferFunction(num, den, dt=smapleing_time)
    stsd = cont2discrete((num, den), method='bilinear', dt=smapleing_time)
    tout, yout = dlsim(stsd, u=input_data)
    return tout, yout


def model_system(a, b, zeta, wn):
    """
      b                  wn * wn
    ----- * -----------------------------------  -> close loop system
    s + a    s^2 + 2 * zeta * wn * s + wn * wn
    """
    num = [b * wn * wn]
    den = [1, a + 2 * zeta * wn, wn * wn + 2 * zeta * a * wn, (a + b) * wn * wn]
    return num, den


if __name__ == '__main__':
    a = 1
    b = 20
    zeta = 0.707
    wn = 1000
    # num = [10]
    # den = [1, 10]
    num, den = model_system(a, b, zeta, wn)
    smaple_time = 0.01
    input_data = np.ones(300)
    sysd = cont2discrete(model_system(a, b, zeta, wn), method='bilinear', dt=smaple_time)
    tout, yout = control_num_den(num, den, smaple_time, input_data)
    plt.plot(tout, yout)
    print(yout)
    plt.show()
