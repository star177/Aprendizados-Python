# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:13:46 2024

@author: julia
"""

def fat(x):
    if x > 1:
        i = 1
        fat = x 
        while i<x :
            fat = fat * i
            i = i + 1
    if x == 0:
        fat = 1
            
    if x == 1:
        fat = 1
    return (fat)

def escolha():
    print("Digite '1' para saber o fatorial de uma sequência")
    print("Digite '2' para saber o fatorial de apenas um número")
    resp = int(input(""))
    while resp != 1 and resp != 2:
        print()
        print("Escolha inválida, tente novamente.")
        print()
        print("Digite '1' para saber o fatorial de uma sequência")
        print("Digite '2' para saber o fatorial de apenas um número")
        resp = int(input(""))
    return(resp)

def continuar():
    print()
    print("Deseja criar mais uma sequência ou ver o fatorial de mais algum número?")
    cont = str(input(""))
    continua = False
    while cont != "sim" and cont != "Sim" and cont != "Não" and cont != "não" and cont !=  "nao" and cont != "Nao":
        print("Resposta inválida (digite algo como 'sim' ou 'não')")
        print()
        print("Deseja criar mais uma sequência ou ver o fatorial de mais algum número?")
        cont = str(input(""))

    if cont == "sim" or cont == "Sim":
        continua = True
        
    else:
        continua = False
    return(continua)


def main():
    print("~~~ Bem vindo ao meu programa. Veja o fatorial do(s) número(s) que desejar! ~~~")
    print()
    resposta = escolha()
    if resposta == 1:
        print("Informe quantos termos haverá na sua sequência: ")
        seq = int(input(""))
        i = 1
        while i <= seq:
            num = int(input("Digite o %dº termo da sequência: " %(i)))
            if num < 0:
                print("Número inválido, não existe fatorial de números negativos pois sempre daria igual a zero. O fatorial de um número indica o produto desse número com todos números inteiros menores que eles até 1.")
                num = int(input("Digite o %dº termo da sequência: " %(i)))
            print(num, "! = ", fat(num), sep = "")
            i = i + 1
        print("Fim da sua sequência.")
        
    if resposta == 2:
        num = int(input("Digite seu número: "))
        print("O fatorial de %d é %d" %(num, fat(num)))
    cont = continuar()
    if cont:
        main()
    if not cont:
        print()
        print("~~~ Até a próxima! ~~~~")
    
main()