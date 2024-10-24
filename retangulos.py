# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:18:42 2024

@author: julia
"""

#programa 

def retangulo_cheio(): 
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
    
def retangulo_vazado():
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
        
def continuar():
    print()
    print("Deseja fazer mais retângulos?")
    cont1 = str(input(""))
    cont = cont1.lower()
    continua = False
    while cont != "sim" and cont != "não" and cont != "nao":
        print("Resposta inválida (digite algo como 'sim' ou 'não')")
        print()
        print("Deseja fazer mais retângulos")
        cont = str(input(""))

    if cont == "sim":
        continua = True
        
    if cont == "não" or cont == "nao":
        continua = False
    return(continua)        
        
def main():
    print()
    print("*** Olá, seja bem-vindo ao meu programa ***")
    print("transforme um  valor de largura e um de altura em um retângulo formado por caracteres '#'")
    print()
    print("você deseja:")
    print("1 - retângulo cheio")
    print("2 - retângulo vazio por dentro")
    resp = int(input(""))
    print()
    if resp != 1 and resp != 2:
        while resp != 1 or resp != 2:
            print("Resposta inválida, tende novamente.")
            print("1 - retângulo cheio")
            print("2 - retângulo vazio por dentro")
            resp = int(input(""))
            print()
    if resp == 1:
        retangulo_cheio()
        
    if resp == 2:
        retangulo_vazado()
        
    cont = continuar()
    
    if cont:
        main()
        
    if not cont:
        print()
        print("*** Até a próxima!! ***")
    
main()
        
    