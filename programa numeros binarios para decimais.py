# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:49:36 2024

@author: julia
"""

def binários_para_decimais():
    num = int(input("Digite um número: "))
    clone = num
    tamanho = 1
    resultado = 0
    
    while resultado != num:
        resultado = num % 10**tamanho
        tamanho = tamanho + 1
        
        
    tamanho = tamanho - 1
    tam = tam2 = tamanho
    

    lista = []  
        
    
    while tam > 0:
        tam = tam - 1
        lista.append(clone % 10)
        clone = clone // 10
        
    soma = 0 
    expoente = 0
    t = 0
    while t < tam2:
        numero = lista[t]
        expoente = (2**t) * numero
        soma = soma + expoente 
        t = t + 1    
        
    print("Seu número corresponde à:", soma)
    
    return(soma)

    
    