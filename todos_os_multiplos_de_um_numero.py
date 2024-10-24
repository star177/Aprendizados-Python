# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:04:51 2024

@author: julia
"""
print()
print("***    Bem-Vindo ao meu programa    ***")
print()
print("O intuito deste programa é escrever um número e ver a quantidade de múltiplos (tirando o 0) que desejar.")
print()
num = int(input("Digite um número: "))
maxi= int(input("Digite quantos múltiplos desse número deseja ver (tirando o 0): "))
maxi = (maxi * num) + num

if num == 0: 
    print(0)

if num != 0:
    for i in range (num, maxi, num):
        if i == maxi - num:
            print(i, ".", sep="")
        else:
           print(i, ", ", sep="", end="") 
        