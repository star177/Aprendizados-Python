# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:55:01 2024

@author: julia
"""

n_salvo = n = int(input("Digite um numero: "))

anterior = n % 10
n = n // 10;
adj_iguais = False;
while n > 0 and not adj_iguais:
    atual = n % 10
    if atual == anterior:
        adj_iguais = True 
    anterior = atual
    n = n // 10

if adj_iguais:
    print("sim")
else:
    print("não")