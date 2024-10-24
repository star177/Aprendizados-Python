# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:09:30 2024

@author: julia
"""
print("n!")
num = int(input("digite um número para saber seu fatorial: "))
k = 1
fatorial = num
while k < num:
    fatorial = fatorial * (num - k)
    k = k + 1
    
if num  == 0 or num == 1:
    fatorial = 1
print(fatorial)
    