# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:52:42 2024

@author: julia
"""
n = int(input("n; "))
m = int(input("m; "))


def computador_escolhe_jogada(n, m):
    mult = m + 1
    i = 1
    resto = m
    while resto % mult != 0:
        resto = n - i
        if resto % mult == 0:
            return(i)
        else:
            i = i+1
        
print (computador_escolhe_jogada(n, m))
