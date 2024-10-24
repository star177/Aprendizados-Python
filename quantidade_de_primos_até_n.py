# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:49:48 2024

@author: julia
"""

def n_primos(x):
    d = 1
    k = 2
    primos = 0
    while k <= x:
        d = 0
        divisor = 1
        while divisor < k:
            if (k % divisor == 0):
                d = d + 1
            else:
                d = d + 0
            divisor = divisor + 1
        if d == 1:
            primos = primos + 1
        k = k + 1
    return(primos)