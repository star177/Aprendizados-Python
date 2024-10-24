# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:44:32 2024

@author: julia
"""
#programa que diz a soma de todas as hipotenusas formadas por números cuja a soma da "n"
def é_hipotenusa(n):
    i = 1
    j = 1
    h = n
    hipotenusa = False
    while i < n:
        j = 1
        while j <= n:
            h = (i**2 + j**2)**(1/2)
            if h % 1 == 0 and h == n:
                hipotenusa = True    
            j = j + 1
        i = i + 1
    return(hipotenusa)

def soma_hipotenusas(n):
    h = 0
    soma = 0
    while h <= n:
        hip = é_hipotenusa(h)
        if hip == True:
            soma = soma + h
        h = h + 1
    return(soma)
    

    
    