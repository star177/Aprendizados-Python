# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:30:39 2024

@author: julia
"""

num = num_salvo = num_salvo_2 = int(input("num: "))


if num == -1:
    print("o número -1 em binário corresponde a 1111.")



if num < 0 and num != (-1):
    num = num * (-1)
    num_salvo = num
   
        
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
    
    if num_salvo == 8:
        str_binario = "00"
    
    str_binario = "10" + str_binario
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


    while k > 0:
        nova = binarios%10
        if nova == 1:
            str_nova_2 = "0"
        if nova == 0:
            str_nova_2 = "1"
        if k == k_salvo:
            str_binario_2 = str_nova_2
        if k != k_salvo:
            str_binario_2 = str_nova_2 + str_binario_2
        k = k - 1
        binarios = binarios // 10
            
    binarios = binarios_salvo = int(str_binario_2)
    k = k_salvo_2 = contadigitos(binarios) 
        
    

    somanova = 0
    i = 0
    adicional = 0
    while i < 1 or (k_salvo_2 >= 1 and k >= 0) or (adicional != 0):
        if k <= 0:
            resto = 0   
        
            resto = binarios % 10
        if k == k_salvo_2 and k>0:
            resto = binarios % 10
            somanova = resto + 1 + adicional
        if k != k_salvo_2:
            resto = binarios % 10
            somanova = resto + adicional
            
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
        
    somabinario = int(str_soma)
    
    print("o número decimal", num_salvo_2, "corresponde à", somabinario, "em números binários (pelo complemento de 2).")
    
if num_salvo_2>=0:
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