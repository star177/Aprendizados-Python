# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:16:41 2024

@author: julia
"""
#Strings > Módulo 2

#acessar todos os caracteres:
string = "String"
print(string[0])
    
#upper: converte todos os caracteres para letras maiusculas
#lower: faz o contrario
print(string.upper())
print(string.lower())

#capitalize: deixa a primeira letra maiusula e o resto minuscula
print(string.capitalize())

#strip remove espaços em branco do começo e do fim

#count fala quantas ocorrencias de um caractere
print(string.count("n"))

#replace substitui um pedaço
print("Eu torço para o Corinthians".replace("Corinthians", "São Paulo"))

#capitalize com center: centraliza em uma quantidade de caracteres
print(string.capitalize().center(50))

#find: mostra a posicao do caractere procurado, ele da -1 quando nao  tem
print(string.find("g"))
print(string.find("in"))
print(string.find("a"))

#len: tamanho
print(len(string))

#intervalos
fruta = "amora"
print(fruta[:4])
print(fruta[2:4])

