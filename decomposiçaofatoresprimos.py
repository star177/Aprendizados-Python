# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:04:50 2024

@author: julia
"""
#decomposição em números primos:

def main():
    
    num = int(input("digite um número: "))
    numsalvo = num
    div = 2 
    
    while num != 1:
        mult = 0
        while num % div == 0:
            mult = mult + 1 
            num = num / div
            
        if mult != 0:
            print("o %d, divide por %d, %d vezes - fator %d, multiplicidade %d" %(numsalvo,div,mult,div,mult))
        
        div = div + 1 
        
main()