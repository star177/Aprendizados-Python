# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:39:06 2024

@author: julia
"""

num = int(input("digite um número para saber a soma entre seus digitos: "))
soma = 0
k = num % 10

while num != 0:
    soma = soma + k
    num = num // 10
    k = num % 10
    
print(soma)