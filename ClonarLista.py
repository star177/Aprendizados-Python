# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 06:19:36 2024

@author: julia
"""

#Clonar Listas

def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone


print(clone)