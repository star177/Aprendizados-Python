# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:45:50 2024

@author: julia
"""

num = int(input("Digite uma sequência [acabada em 0]: "))
lista = []
lis = []
while num != 0:
    lista.append(num)
    num = int(input("Digite um número [0 para acabar]: "))
    
maximo_salvo = len(lista)
i = -1
maximo = maximo_salvo * (-1)

while i >= maximo:
    num = lista[i]
    lis.append(num)
    i = i - 1
    
print(lis)
    

    