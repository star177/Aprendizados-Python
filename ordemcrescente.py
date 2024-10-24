# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:36:15 2024

@author: julia
"""

a = int(input("escreva o primeiro número: "))
b = int(input("escreva o segundo número: "))
c = int(input("escreva o terceiro número: "))

k = 0

while k<1:
    if (a<b<c) or (c<b<a):
        medio = b
        k = k+1
        if a<b<c:
            menor = a
            maior = c
        if c<b<a:
            menor = c
            maior = a
            
    if (b<a<c) or (c<a<b):
        medio = a
        k = k + 1
        if b<a<c:
            menor = b
            maior = c
        if c<a<b:
            menor = c
            maior = b
    if (a<c<b) or (b<c<a):
        medio = c
        k = k + 1
        if a<c<b:
            menor = a
            maior = b
        if b<c<a:
            menor = b
            maior = a
            
print ("ordem crescente: %d - %d - %d" %(menor,medio,maior))
