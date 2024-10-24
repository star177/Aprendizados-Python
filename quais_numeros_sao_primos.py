# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:25:39 2024

@author: julia
"""

def main(): 

        print("saiba quais os numeros primos da sua sequência.")
        q = int(input("Digite a quantidade de números da sequência: ")) 
        num = int(input("escreva um número: "))
        k = 0 #contador
        cont = 0 #contador de numeros primos
        while k < q: 
            str_num = str(num) #transformador do num em string
            primo = True
            i = 2
            while i < num and primo: 
                if num % i == 0: 
                    primo = False 
                i += 1 
            if primo:
                cont = cont + 1 #saber quantos numeros primos tem
                
            if cont == 1 and primo:
                primos = str_num
             #se so houver um primo transformar o "primos" na "str_num
            elif cont > 1 and primo:  
                primos = primos + ', ' + str_num
           #se houver mais de um numero primo somar as strings
                
            k = k + 1 #para acabar a sequencia
            
            if k < q:  #se for o ultimo numero nao perguntar pelo proximo numero
                num = int(input("escreva um número: "))
                
            
        if cont > 0:
            primos = primos 
        if cont == 0: #se nao houver numeros primos -> para nao dar erro
            primos = '   '               
        print("Nesta sequência, há", cont, "números primos:", "[", primos, "]")
        
        
      
main()

          