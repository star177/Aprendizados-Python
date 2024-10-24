# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:12:08 2024

@author: julia
"""

a = int(input("digite 'a': "))
b = int(input("digite 'b': "))
c = int(input("digite 'c': "))

delta = (b**2) - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")

if delta == 0:
    x1 = (-b + ((b**2) - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - ((b**2) - 4*a*c)**(1/2))/(2*a)
    if x1 == 0:
        print("a raiz desta equação é", x2)
    else: 
        print("a raiz desta equação é", x1)
        
if delta > 0:
    x1 = (-b + ((b**2) - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - ((b**2) - 4*a*c)**(1/2))/(2*a)
    if x1 != x2 and x1<x2:
        print("as raízes da equação são", x1, "e", x2)
    if x1 != x2 and x2<x1:
        print("as raízes da equação são", x2, "e", x1)
    if x1 == x2:
        print("a raiz dupla desta equação é", x1)