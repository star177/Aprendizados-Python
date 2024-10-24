# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:18:28 2024

@author: julia
"""

def main():    

    print("contagem de numeros primos na sequencia")
    num = int(input("escreva um número [0 para terminar]: "))

    cont = 0
    while num != 0:
        primo = True
        i = 2
        while i < num and primo:
            if num % i == 0:
                primo = False
            i += 1
        if primo:
            cont += 1
    
        num = int(input("escreva um número [0 para terminar]: "))
                  
    print ("a contagem é de %d números primos"%(cont))                        

#--------------------------
main()           