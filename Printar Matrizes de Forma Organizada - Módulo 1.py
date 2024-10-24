# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:13:27 2024

@author: julia
"""



def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len((matriz[0]))
    
    
    for h in range(linhas):
        linha = ""
        for j in range(colunas):
            numero = str(matriz[h][j])
            espaco = ' '
            if j == 0:
                linha = numero
            else:
                linha = linha + espaco + numero
        print(linha)
            
matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(matriz)