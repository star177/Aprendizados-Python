# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:45:08 2024

@author: julia
"""

print("você deseja converter:")
print("a) decimal para binário")
print("b) binário para decimal")
resposta = input("digite 'a' ou 'b': ")

if resposta == "a":
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
    
if resposta == "b":
    num = num_salvo = int(input("digite um número binário para converter em decimal: "))
    i = k = soma = 0
    divisao = d = 10

    while divisao > 1: 
        divisao = num // (d**k)
        k = k + 1

    while k > 0:
        resto = num % 10 
        dec = resto * (2**i)
        i = i + 1
        num = num // 10
        soma = soma + dec
        k = k - 1

    print("o número", num_salvo, "em binário, corresponde à", soma, "em decimal.")    