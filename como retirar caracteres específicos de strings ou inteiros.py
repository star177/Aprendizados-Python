# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:34:56 2024

@author: julia
"""
#retirada de caracteres especiais de strings
lista_usuario = input("Digite os itens da matriz numa lista: ")
retirada = '[], '

for i in retirada:
    lista_usuario = lista_usuario.replace(i, '')
    
print(lista_usuario)