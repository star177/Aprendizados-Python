# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:31:27 2024

@author: julia
"""

num = num_salvo = int(input("num: "))

num = num * (-1)
num_salvo = num



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
        
binarios = int(str_binario)
        
binariopositivo = binarios
        
num = num_salvo


def contadigitos(x):
    menor = True
    k = 1
    while menor:
        if x > 10**k:
            menor = True
        if x < 10**k:
            menor = False
        k = k + 1
    k = k - 1
    return(k)

k = k_salvo = contadigitos(binarios)

somanova = 0
i = 0
adicional = 0
while i < 4 or (k_salvo >= 4 and k >= 0 and adicional != 0):
    if k <= 0:
        resto = 0   
    if k > 0:
        resto = binarios % 10
        
    somanova = resto + 1 + adicional
        
    adicional = 0
    if somanova >= 2:
        adicional = 1
        if somanova == 2:
            somanova = 0
        if somanova == 3:
            somanova = 1
            
    str_somanova = str(somanova)
    if i == 0:
        str_soma = str_somanova
    if i != 0:
        str_soma = str_somanova + str_soma
    i = i + 1
    binarios = binarios // 10
    k = k - 1
    
str_soma = "1" + str_soma
somabinario = int(str_soma)  
k = k_salvo_2 = contadigitos(somabinario)   

str_binario_2 = " "
while k > 1:
    nova = somabinario%10
    if nova == 1:
        str_nova_2 = "0"
    if nova == 0:
        str_nova_2 = "1"
    str_binario_2 = str_nova_2 + str_binario_2
    k = k - 1
    somabinario = somabinario // 10
    
print(binariopositivo, k_salvo, str_soma, k_salvo_2, str_binario_2)

    


        
        
        
        
        