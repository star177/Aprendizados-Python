# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:51:45 2024

@author: julia
"""

linha = int(input("largura: "))
quantlinhas = int(input("altura: "))
j = 1
i = 1
while i <= quantlinhas:
    j = 1
    while j <= linha:
        print("#", end = "")
        j = j + 1
    print()
    i = i + 1
    