# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:47:57 2024

@author: julia
"""
num = int(input("digite um número para saber qual o maior número primo igual ou menos que ele: "))

def maior_primo(x):
    d = 1
    k = 1
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
            maiorprimo = k
            
        k = k + 1
    return maiorprimo

print("o maior número primo até ", num, ", é o ", maior_primo(num), ".", sep='')