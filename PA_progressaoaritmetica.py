# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:07:48 2024

@author: julia
"""
#progressao aritmetica

seq = int(input("digite quantos termos terão na sequência: "))
num = int(input("digite um número da sequência: "))
x = 0
k = 0
num_inicial = num 
salvo = num_inicial
soma = 0

while k < seq:
    if k == 0:
        num = int(input("digite um número da sequência: "))
        x = num - num_inicial
        k = k + 1
        
    if (k == seq - 1): 
        soma = num + num
        k = k + 1
        if num < num_inicial:
            num_inicial = num
            num = salvo
            #se a sequencia estiver do maior para o menor:
    #o "num_inicial" vira o numero mais atualizado (numero final "num")
    #e o numero final vira o primeiro colocado o "salvo"
    else:
        num = int(input("digite um número da sequência: "))  
        soma = num + num
        k = k + 1

if x < 0:
    x = x * (-1)
#x positivo[ modulo] - ja que é a difereça entre os termos e nao a soma deles  
    
if(num_inicial == num - (seq - 1)*x): 
    print("essa sequência é uma progressão aritmética, e tem uma diferença de", x, "entre os termos da sequência.")
          
else:
    print("essa sequencia não é uma progressão aritmética.")
