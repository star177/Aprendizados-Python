# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:47:10 2024

@author: julia
"""

def subtraçao(x, y):
    k = 0
    divisao = d = 10
    o = 0
    m = 0   
    while divisao > 1: 
        divisao = num_salvo // (d**k)
        k = k + 1
        o = num % 10
        num = num // 10
        k_salvo = k
        
    while k < 0:
        a = x % 10
        b = y % 10
        sub = a - b
        if sub == -1:
            sub == 0
            a = 0
            
        str_nova = str(sub)
        if k == k_salvo:
            str_sub = str_nova
            
        else: 
            str_sub = str_nova + str_sub
        