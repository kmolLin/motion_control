# -*- coding: utf-8 -*-

import yaml
from numpy import pi
from core.forward_kinematics import forward_transform
from core.inverse_kinematics import inverse_transform
from core.nc import nc_code_compiler
from core import print_matrix


if __name__ == '__main__':
    nc_code_compiler("line.nc")
