# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:49:33 2024

@author: julia
"""
#dá a quantidade de termos que você quiser dos multiplos de i, de j, ou de ambos

def main ():
    n = int(input("escreva n: "))
    i = int(input("escreva i: "))
    j = int(input("escreva j: "))
    
    mult_i = mult_j = 0
    
    k = 0
    
    while k < n:
        if mult_i == mult_j:
            print(mult_i)
            mult_i = mult_i + i
            mult_j = mult_j + j
        elif mult_i < mult_j :
            print(mult_i)
            mult_i = mult_i + i
        else:
            print(mult_j)
            mult_j = mult_j + j
                
        k = k + 1
        
main()
                
        