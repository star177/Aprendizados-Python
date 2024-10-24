# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:18:14 2024

@author: julia
"""

print("Descubra se todos os números da sua sequência são pares.")
n = int(input("escreva a quantidade de termos na sequência: "))
par = True 
k = 0
par = impar = 0

while k < n:                           
    num = int(input("número: "))
    if num % 2 == 0:
        par = par + 1
    else: 
        impar = impar + 1
    k = k + 1

if (par == n):
    print("Sim, todos os números da sequência são pares.")
    
else: 
    print("Não, há números impares em sua sequência.")