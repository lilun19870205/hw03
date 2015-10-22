# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:34:24 2015

@author: lilun
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math
from sympy.solvers.polysys import solve_triangulated
from sympy.abc import x, y, z


def equations(p):
    x,y=p
    return(x**2+y**2-1, x-y-10)
z=np.array([(1,1),(-1,-1)])
a=fsolve(equations,(0,0))