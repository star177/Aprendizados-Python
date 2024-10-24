# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:31:34 2024

@author: julia
"""
n = int(input("n; "))
m = int(input("m; "))


def usuario_escolhe_jogada(n, m):
    jogador = int(input("Quantas peças você vai tirar? "))
    if jogador <= m and jogador > 0:
        return(jogador)
    else:
        while jogador > m or jogador <= 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            jogador = int(input("Quantas peças você vai tirar? "))
        return(jogador)
    
print(usuario_escolhe_jogada(n, m))