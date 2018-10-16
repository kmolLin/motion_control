# -*- coding: utf-8 -*-

import yaml
from numpy import pi
from core.forward_kinematics import forward_transform
from core.inverse_kinematics import inverse_transform
from core import print_matrix


if __name__ == '__main__':
    with open("BZYXC_5_axis.yml", 'r') as f:
        data = yaml.load(f.read())

    r_t = forward_transform(82.250, 0, -82.25, pi / 2, -pi / 2, **data)
    print_matrix(r_t)

    result = inverse_transform(0., 0., 0., 0., 0., 1., **data)
    print(result)
