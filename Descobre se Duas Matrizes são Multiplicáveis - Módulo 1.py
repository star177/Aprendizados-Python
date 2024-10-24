# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:20:54 2024

@author: julia
"""

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        multiplicaveis = True
    else:
        multiplicaveis = False
    return(multiplicaveis)