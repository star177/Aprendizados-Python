# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:16:51 2024

@author: julia
"""

def main():
    
    
    def inicio():
        num = int(input("Digite um número: "))

        resultado = num
        resto = 0
        lista = []
        
        while resultado >= 1 and num != 0 and num != 1:
            if resultado == 1:
                resto = 1
            else:
                resto = resultado % 2   
            resultado = resultado // 2
            lista.append(resto)
        if num == 0:
            lista = [0]
        if num == 1:
            lista = [1]
            
        return(lista)
        
    def lista_nova(lista):
        tamanho = len(lista)
        tamanho = tamanho * -1
        i = 0
        listanova = []
        numero = 0
        
        while i != tamanho:
           i = i - 1 
           numero = lista[i]
           listanova.append(numero)
           
        return(listanova) 
            
  

    def formador_de_string(listanova):
        str_binario = ''
        tamanho = len(listanova)
        i = 0
        numero = 0
        while i < tamanho:
            numero = listanova[i]
            str_binario = str_binario + str(numero)
            i = i + 1
            
        print("Binário:", str_binario)
        return(str_binario)
    



    print("Bem-Vindo(a)")
    print("Passe qualquer número de decimal para binário ou vise-versa!")
    formador_de_string(lista_nova(inicio()))
    
    

    
main()