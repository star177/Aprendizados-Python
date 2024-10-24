# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:49:45 2024

@author: julia
"""

#MATRIZES - Módulo 1 > Matrizes

#lista de listas

#Ex:
    
A = [[1,2,3],
     [4, 5, 6],
     [7, 8, 9]]
     
#Lembrete: o comando range() passa por todos os itens de uma lista
#menos o último.

#ex:
#for i in range(9):
#    print(i)
#vai passar por todos os números de 0 à 8.


#modelo:

def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) -> matriz (lista de valores)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário.
    '''
    
    matriz = [] #lista vazia 
    for i in range(num_linhas):
        #cria a linha número i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento[" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
            
        #adiciona alinha à matriz
        matriz.append(linha)
    
    #para ficar organizado é importante colocar em linhas separadas a lista
   
    #Antes:
    #matriz = [[1,2,3], [4,5,6], [7,8,9]]
    
    #Depois:
    #[1, 2, 3]
    #[4, 5, 6]
    #[7, 8, 9]
    
    #organização da lista:
    for h in range(num_linhas):
        print(matriz[h])
        
    return matriz
        
def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin,col)


#Caso o usuario queira colocar diretamente uma lista para criar a matriz 
#enves de colocar os itens um por um:
#lista_usuario = input("Digite os itens da matriz numa lista: ")
#retirada = '[], '

#for i in retirada:
#    lista_usuario = lista_usuario.replace(i, '')

#Ex:
 
#def le_matriz continua
def le_matriz_2():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz_2(lin,col)


def cria_matriz_2(num_linhas, num_colunas):
    ''' (int, int) -> matriz (lista de valores)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário.
    '''
    
#para evitar as aspas em todos os itens da lista de números podemos:
    
    
        
    lista_usuario = input("Digite os itens da matriz numa lista: ")
    retirada = '[], '
    
    for i in retirada:
        lista_usuario = lista_usuario.replace(i, '')
        #tirar todos os  aracteres especiais e criar uma str
        
    valores = list(lista_usuario)
    maximo = num_colunas * num_linhas
    k = 0
    while k < maximo:     
        num = valores[k]
        retirada = " ' "
        for i in retirada:
            num = num.replace(i, '')
        valores[k] = int(num)
        k = k + 1
        #fazer uma lista com inteiros
    
            
            
        
        
#TESTES de execução dos códigos

le_matriz()