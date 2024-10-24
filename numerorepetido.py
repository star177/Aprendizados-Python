# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:57:24 2024

@author: julia
"""

print("veja quantas dezenas ou centenas se repetem apenas duas vezes no seu número")
tam = int(input("coloque quantos digitos terá o número: "))
num = int(input("escreva um número: "))
k = 0
d = 0 
resto = 0
num_salvo = num
e = 10
while k < tam:                  
    d = num//10
    resto = num_salvo % e                       
    e = e * 10  
    k = k + 1
    num = d
    
    if (d == resto) and (d != 0):         
        k = tam
        
if (d == resto) and (d != 0):
    print(d, "se repete duas vezes no número", num_salvo)
    
else: 
    print("nenhuma dezena ou centena se repete duas vezes no número", num_salvo)
