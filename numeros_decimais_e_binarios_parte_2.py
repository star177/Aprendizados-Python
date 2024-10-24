# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:48:36 2024

@author: julia
"""

num = num_salvo = int(input("digite um número para converter em binário ou decimal: "))
i = k = soma = 0
divisao = d = 10
binario = True
o = 0

while divisao > 1 and binario: 
    divisao = num_salvo // (d**k)
    k = k + 1
    o = num % 10
    if o == 1 or o == 0:
        binario = True
    else:
        binario = False
    num = num // 10
    
    
num = num_salvo    
 
if binario:        
    while k > 0:
        resto = num % 10 
        dec = resto * (2**i)
        i = i + 1
        num = num // 10
        soma = soma + dec
        k = k - 1
    print("o número", num_salvo, "em binário, corresponde à", soma, "em decimal.") 
 
 
if num_salvo == 0:
   str_binario = "0"
        
if num_salvo == 1:
    str_binario = "1"
       
num = num_salvo

while num != 1 and num != 0:
    str_nova = str(num%2)
    if num_salvo == num:
        str_binario = str_nova
    if num_salvo != num and num != 1:
        str_binario = str_nova + str_binario
    num = num // 2
    if num == 1:
        str_nova = "1"
        str_binario = str_nova + str_binario
        binarios = int(str_binario)
print("o número", num_salvo, " em decimal, corresponde à", str_binario, "em números binários.")