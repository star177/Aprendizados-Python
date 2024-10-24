# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 07:13:10 2024

@author: julia
"""

def remove_repetidos(lista):
    sem_repeticao = []
    i = 0
    sem_repeticao = list(set(lista))
    sem_repeticao.sort()
    
    return(sem_repeticao)
        