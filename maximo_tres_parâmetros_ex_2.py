# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:36:00 2024

@author: julia
"""


def maximo(x, y, z):
    if x > y:
        if x >= z:
            return(x)
        if x <= z:
            return(z)
    if y >= x:
        if y >= z:
            return(y)
        if y <= z:
            return(z)
