# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:15:34 2024

@author: julia
"""

print("Veja qual a Média Aritmética dos números digitados.")
print()
termos = int(input("digite quantos termos deseja ver a Média Aritmética: "))

k = 0
i = 1
soma = 0
media = 0

print()

while k < termos:
    num = int(input("digite o %do número da sequência: " %(i)))
    
    if k == 0:
        soma = num 
        str_media = str(num)
        
    if k > 0: 
        soma = soma + num
        str_media = str_media + ", " + str(num)
        
    k = k + 1
    i = i + 1
    
media = soma / termos
        

    
print("A média dos números:", str_media)
print("É de:", media)