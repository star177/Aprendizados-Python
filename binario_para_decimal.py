# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:11:06 2024

@author: julia
"""

num = num_salvo = int(input("digite um número binário para converter em decimal: "))
i = k = soma = 0
divisao = d = 10

while divisao > 1: 
    divisao = num // (d**k)
    k = k + 1

while k > 0:
    resto = num % 10 
    dec = resto * (2**i)
    i = i + 1
    num = num // 10
    soma = soma + dec
    k = k - 1

print("o número", num_salvo, "em binário, corresponde à", soma, "em decimal.")    
