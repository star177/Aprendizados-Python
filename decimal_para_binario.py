# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:42:31 2024

@author: julia
"""

num = int(input("digite um número em decimal para converter em número binário: "))
num_salvo = num

if num == 0:
    str_binario = "0"
    
if num == 1:
    str_binario = "1"
    
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
print("o número", num_salvo, "corresponde à", str_binario, "em números binários.")
            