# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:56:18 2024

@author: julia
"""


linha = int(input("largura: "))
quantlinhas = int(input("altura: "))
j = 1
i = 1
a = 1
while i <= quantlinhas:
    
    j = 1
    
    if i == 1:
        while j <= linha:
            print("#", end = "")
            j = j + 1
    if i != 1 and i != quantlinhas:
        while j <= linha:
            if j == 1:
                print("#", end = "")
            if j != 1 and j != linha:
                print(" ", end = "")
            if j == linha:
                print("#", end = "")
            j = j + 1
    if i == quantlinhas:
        while j <= linha:
            print("#", end = "")
            j = j + 1   
    print()
    i = i + 1
    a = a + 1