# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:54:36 2024

@author: julia
"""

#somador de matrizes

def linhas(matriz):
    linhas = len(matriz)
    return(linhas)

def colunas(matriz):
    colunas = len((matriz[0]))
    return(colunas)

def soma_matrizes(m1, m2):
    
    linhasm1 = linhas(m1)
    colunasm1 = colunas(m1)
    linhasm2 = linhas(m2)
    colunasm2 = colunas(m2)
    lin = col = 0
    
    if linhasm1 != linhasm2 or colunasm1 != colunasm2:
        tamanho = False
        return(tamanho)
    
    else:
        matriz = [] 
        for i in range(linhasm1):
            linha = []
            for j in range(colunasm1):
                valor = m1[lin][col] + m2[lin][col]
                col = col + 1
                linha.append(valor)
            lin = lin + 1
            col = 0
            matriz.append(linha)
        return(matriz)
        
