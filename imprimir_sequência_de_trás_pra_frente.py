# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 08:26:10 2024

@author: julia
"""


num = 2
lista = []
while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        lista.append(num)
    
maximo = len(lista)
maximo = maximo * -1
i = -1
while i >= maximo: 
    print(lista[i])
    i = i - 1