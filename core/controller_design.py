# -*- coding: utf-8 -*-
from scipy.signal import TransferFunction, dlsim, dstep, step, cont2discrete
import numpy as np
import matplotlib.pyplot as plt


def control_num_den(num, den, smapleing_time, input_data):

    # tf = TransferFunction(num, den, dt=smapleing_time)
    stsd = cont2discrete((num, den), method='bilinear', dt=smapleing_time)
    tout, yout = dlsim(stsd, u=input_data)
    return tout, yout


if __name__ == '__main__':
    num = [10]
    den = [1, 10]
    smaple_time = 0.01
    input_data = np.ones(300)
    sysd = cont2discrete((num, den), method='bilinear', dt=smaple_time)
    tout, yout = control_num_den(num, den, smaple_time, input_data)
    plt.plot(tout, yout)
    plt.show()

