# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:05:44 2024

@author: julia
"""

numero = int(input("digite um número: "))
k = 10
dezenas = 1
dez = -9

while dez == -9:
    dezenas = numero % k
    if dezenas > 9 and dezenas < 100 or dezenas == 0: #100>dezenas>9
        dez = dezenas // 10
    k = k * 10
    if numero < 10:
        dez = 0

print("O dígito das dezenas é %d" %(dez))
    
# k = 10 
# while: 100>dezena>9
# 167 % 10 = 7
#   100 > "7" < 9 = False
#  k = k * 10

#167 % 100 = 67
#100 > 67 > 9 = True
#  dez = 67 // 10 = 6
