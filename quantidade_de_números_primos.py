# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:53:13 2024

@author: julia
"""

print("Veja a quantidade desejada de números primos.")
print()
quantidade = int(input("Escreva quantos números primos que deseja ver: "))
d = 1
k = 1
primos = 0
while primos < quantidade:
    d = 0
    divisor = 1
    while divisor < k:
        if (k % divisor == 0):
            d = d + 1
        else:
            d = d + 0
        divisor = divisor + 1
    if d == 1:
        primos = primos + 1
        if primos < quantidade:
                print(k, ", ", sep='', end='')
        if primos == quantidade:
                print(k, end='.')
    k = k + 1

        