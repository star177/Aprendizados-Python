# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:15:09 2024

@author: julia
"""

# Função que recebe uma lista de nomes e devolve o menor em ordem lexicográfica

lista = ["Joao", "maria", "ANA", "ANU"]

def funcao(lista):
    
    tam_lista = len(lista)
    
    for i in range(tam_lista):
        lista[i] = lista[i].strip().lower()
        
    for h in range(tam_lista):
        if h == 0:
            string = str(lista[h])
            salvo = h
        else:
            if str(lista[h]) <= string:
                string = str(lista[h])
                salvo = h
            
    return(lista[salvo])

print(funcao(lista))