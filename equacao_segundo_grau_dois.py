# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:07:40 2024

@author: julia
"""
print("ax² + bx + c = 0")
print()
a = int(input("digite o valor de 'a' (ax²): "))
b = int(input("digite o valor de 'b' (bx): "))
c = int(input("digite o valor de 'c' (c): "))

delta = (b**2) - (4*a*c)
    
if delta < 0:
    print("Não há raizes reais para esta equação do segundo grau")
    
if delta == 0:
    raiz_um = ((-b + delta**(1/2))/(2*a))
    raiz_dois = ((-b - delta**(1/2))/(2*a))
    if raiz_um != 0:
        print("A raiz para a equação é: x' =", raiz_um)
    if raiz_dois != 0:
        print("A raiz para a equação é: x' =", raiz_dois)

if delta > 0:
    raiz_um = ((-b + delta**(1/2))/(2*a))
    raiz_dois = ((-b - delta**(1/2))/(2*a))
    
    if raiz_um > raiz_dois:
        print("As raizes para essa equação são: x' =", raiz_um, "e x'' =", raiz_dois)
    else:
        print("As raizes para essa equação são: x' =", raiz_um, "e x'' =", raiz_dois)