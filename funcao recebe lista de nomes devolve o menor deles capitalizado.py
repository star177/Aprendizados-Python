# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:47:00 2024

@author: julia
"""

#Função que recebe uma lista de nomes e devolve o menor nome capitalizado 




lista = ["   AnA   ", "BEATRIZ", "jose"]



def funcao(lista):
    tam_lista = len(lista)
    for i in range(tam_lista):
        lista[i] = lista[i].strip()
    
    
    for h in range(tam_lista):
        if h == 0:
            tam = len(lista[h])
            Salvo = h
        else:
            if tam >= len(lista[h]):
                tam = len(lista[h])
                Salvo = h
            else:
                tam = tam
                
      
    nome = lista[Salvo]
    nome = nome.capitalize()
    
    return(nome)
            
        
print(funcao(lista))