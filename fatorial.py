# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:28:25 2024

@author: julia
"""

#fatorial de cada numero de uma sequencia
# fat = n * (n-i) * (n-i) ...
# i = 1 
# i = i + 1
#enquanto i < n
# 4 = 4 * (4-1) * (4-2) * (4-3) = 4 * 3 * 2 * 1 = fat
#print(fatoriais:)
#print(fat) dentro do while para colocar cada fatorial na lista

def main():
    
    q = int(input("quantidade de numeros: "))
    
    s = 0
    while s < q: 
        num = int(input("digite o %do número: " %(s+1)))
        s = s + 1
        print("%d ! = %d" %(num,fatorial(num)))
        
        
def fatorial(g):
    g_fat = 1
    s = 2
    while s <= g:
        g_fat *= s
        s += 1
        
    return g_fat

main()
    
