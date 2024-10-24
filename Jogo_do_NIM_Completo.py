# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:28:23 2024

@author: julia
"""

def computador_escolhe_jogada(n, m):
    mult = m + 1
    i = 1
    acabou = False
    resto = n - i
    if resto <= m:
        while i<n:
            i = i + 1
        return(i)
    
    else:
        resto = m
        while resto % mult != 0 and not acabou:
            resto = n - i
            if (resto % mult == 0 and i <= m) or (i == m):
                return(i)
                acabou = True
            else:
                if resto == 1 and i<= m:
                    return(i)
                    acabou = True
                if resto == m and i<=m:
                    return(i)
                    acabou = True
                else:
                    i = i+1

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


def partida():
    print()
    n = int(input("Quantas peças no total: "))
    if n <= 1:
        while n <= 1:
            print("Oops! Jogada inválida! Tente de novo.")
            n = int(input("Quantas peças você quer tirar: "))
    m = int(input("Limite de peças por jogada: "))
    if m == n or m<= 0:
        while m == n or m<=0:
            print("Oops! Jogada inválida! Tente de novo.")
            m = int(input("Limite de peças por jogada: "))
    resto = m + 1
    ganhador = " "
    
    if n % resto == 0:
        print()
        print("Você começa!")
        print()
        jogador = usuario_escolhe_jogada(n, m)
        n = n - jogador
        if jogador == 1:
            print("Você tirou uma peça.")
        if jogador != 1:
            print("Voce tirou", jogador, "peças.")
        if n != 1:
            print("Agora restam", n, "peças no tabuleiro")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        print()
        if n == 0:
            acabou = True
        acabou = False
        while not acabou:
            
            
            
            computador = computador_escolhe_jogada(n, m)
            n = n - computador
            
            if computador == 1:
                print("O computador tirou uma peça.")    
            if computador != 1:
                print("O computador tirou", computador, "peças.")
            
            if n == 0:
                acabou = True 
                ganhador = "O computador ganhou!"
                
            if not acabou:
                if n != 1:
                    print("Agora restam", n, "peças no tabuleiro")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                   
            print()
            
            if not acabou:
                jogador = usuario_escolhe_jogada(n, m)
                n = n - jogador
                
            if not acabou and jogador == 1:
                print("Você tirou uma peça.")
            if jogador != 1 and not acabou:
                print("Voce tirou", jogador, "peças.")
                
            if n == 0 and not acabou:
                acabou = True
                ganhador = ("Você ganhou!")
                
            
            if not acabou:
                if n != 1:
                    print("Agora restam", n, "peças no tabuleiro")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                print()
                    
                    
    else:
        print()
        print("Computador começa!")
        print()
        computador = computador_escolhe_jogada(n, m)
        n = n - computador
        if computador == 1:
            print("O computador tirou uma peça.")    
        if computador != 1:
            print("O computador tirou", computador, "peças.")     
        if n != 1:
            print("Agora restam", n, "peças no tabuleiro")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        print()
        acabou = False
        while not acabou:
            
            print()
            
            jogador = usuario_escolhe_jogada(n, m)
            n = n - jogador
            
            if jogador == 1:
                print("Você tirou uma peça.")
            if jogador != 1 and jogador > 0:
                print("Voce tirou", jogador, "peças.")
                
            if n == 0:
                acabou = True
                ganhador = ("Você ganhou!")
                
            if not acabou:
                if n != 1:
                    print("Agora restam", n, "peças no tabuleiro")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                
            print()
                
            if not acabou:
                computador = computador_escolhe_jogada(n, m)
                n = n - computador
                
            if computador == 1 and not acabou:
                print("O computador tirou uma peça.")    
            if computador != 1:
                print("O computador tirou", computador, "peças.")
                
            if n == 0 and not acabou:
                acabou = True 
                ganhador = "O computador ganhou!"
                
            if not acabou:
                if n != 1:
                    print("Agora restam", n, "peças no tabuleiro")
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
    return(ganhador)

                
            
def campeonato():
    print()
    print("Voce escolheu um campeonato!")
    print()
    i = 1
    computador = 0
    usuario = 0
    while i <= 3:
        print()
        print("**** Rodada", i, " ****")
        ganhador = (partida())
        if ganhador == "O computador ganhou!":
            computador = computador + 1
            print()
            print("O computador ganhou!")
        else: 
            usuario = usuario + 1
            print()
            print("Você ganhou!")
        i = i + 1
    return(usuario)



def jogo():
    print()
    print("Bem-vindo ao jogo do NIM! O jogo consiste em escolher um número total de peças e um limite de retirada de peças por jogada. O objetivo é tirar a última peça do jogo. Boa sorte!")
    print()
    print("Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    resposta = int(input(""))
    if resposta == 1:
        print(partida())
    if resposta == 2:
        usuario = (campeonato())
        computador = (3-usuario)
        print()
        print("**** Final do campeonato! ****")
        print()
        print("Placar: você", usuario, "X", computador, "computador")
    else:
        while resposta != 1 and resposta != 2:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            print("1 - para jogar uma partida isolada")
            print("2 - para jogar um campeonato")
            resposta = int(input(""))
            if resposta == 1:
                print(partida())
            if resposta == 2:
                print(campeonato())
                usuario = (campeonato())
                computador = 3 - usuario
                print()
                print("**** Final do campeonato! ****")
                print()
                print("Placar: você", usuario, "X", computador, "computador")    
jogo()
  
