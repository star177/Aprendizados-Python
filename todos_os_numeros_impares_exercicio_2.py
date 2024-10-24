# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:34:07 2024

@author: julia
"""

num = int(input("digite a quantidade de números ímpares que deseja ver: "))
k = 1
i = 0
impar = False
while i < num:
    if k % 2 == 0:
        impar = False
        i = i + 1
    else:
        i = i + 0
        impar = True
    if impar:
        if i < num - 1:
            print(k, ', ', sep='', end='')
        if i == num - 1:
            print(k, ".", sep='')
    k = k + 1