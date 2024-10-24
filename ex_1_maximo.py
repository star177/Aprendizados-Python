# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:46:39 2024

@author: julia
"""


def maximo(x, y):
    if x > y:
        maior = x
    if x < y:
        maior = y
    if x == y:
        maior = x
    return maior
