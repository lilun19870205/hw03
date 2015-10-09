# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:25:26 2015

@author: lilun
"""

import numpy as np
import matplotlib.pyplot as plt

class Point(object) :


    def __init__(self, x, y) :
        self.x, self.y = x, y
    
    def __str__(self) :
        return "Point(%.6F, %.6f) " % (self.x, self.y)

    def __add__(self,other):
        return "Point(%.6F, %.6f) " % (self.x + other.x, self.y + other.y)
    
    def __mul__(self,other):
        return "Point(%.6F, %.6f) " % (self.x * other, self.y * other)
        
    
    
    


