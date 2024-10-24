# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:18:20 2024

@author: julia
"""

print("escreva o termo a, b e c da sua equação de segundo grau [ax² + bx + c = 0]: ")


a = int(input("digite o termo a: "))
b = int(input("digite o termo b: "))
c = int(input("digite o termo c: "))

xum = (-b + (b**2 - 4*a*c)**(1/2))/(2**a)
#a raiz é o **(1/2)
xdois = (-b - (b**2 - 4 * a * c)**(1/2))/(2**a)

print("resultado:", end = '\n' )
print("x' = ", xum, sep = '')
print("x'' = ", xdois, sep = '')

