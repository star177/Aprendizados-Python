# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:25:19 2024

@author: julia
"""

print("você deseja:")
print("a) converter um valor de grau Celsius para Fahrenheit")
print("b) converter um valor de Fahrenheit para Celsius")

resposta = str(input("digite 'a' ou 'b': "))

if resposta == "a":
    C = int(input("digite °C: "))
    F = C*1.8+32
    print("o valor de %d graus Celsius em Fahrenheit é de: %d °F" %(C,F))
    
if resposta == "b":
    F = int(input("digite °F: "))
    C = (5/9)*(F-32)
    print("o valor de %d graus Fahrenheit em Celsius é de: %d °C" %(F,C))
    