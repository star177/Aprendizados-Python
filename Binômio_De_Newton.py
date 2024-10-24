# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:23:34 2024

@author: julia
"""
print()
print("Calcule o binômio de Newton:")
print()
print("n        n!")
print("  = -------------")
print("p   p! * (n - p)!")
print()
n = int(input("digite n: "))
p = int(input("digite p: "))

def fatorial(x):
    i = 1
    mult = x
    if x == 0:
        mult = 1
        i = x
        
    while i < x:
        mult = mult * (x-i)
        i = i + 1
    return mult

binomio = (fatorial(n))//(fatorial(p) * fatorial(n-p))

print(binomio)