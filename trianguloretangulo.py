# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:57:32 2024

@author: julia
"""
#descubra se os números formam um triângulo retângulo
a = int(input("escreva o primeiro número: "))
b = int(input("escreva o segundo número: "))
c = int(input("escreva o terceiro número: "))

if (a**2 == b**2 + c**2) or (b**2 == c**2 + a**2) or (c**2 == a**2 + b**2):
    print("estes números: %d, %d e %d, formam um triângulo retângulo." %(a,b,c))
    
else:
    print("estes números %d, %d e %d não formam um triângulo retângulo." %(a,b,c))