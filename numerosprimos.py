# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:47:31 2024

@author: julia
"""

#exercício 2 - solução minha:
#números primos

print("veja se o número é primo:")
num = int(input("coloque um número: "))
k = 1
d = 0

while k < num:
    if (num % k == 0):
      d = d + 1
#cada divisor de 1 à num soma 1 a "d"
    else:
      d = d + 0
    
    k = k + 1
      
if d == 1:
    print("o número %d é primo, pois seus únicos divisores são 1 e %d." %(num,num))
    
#tirando o próprio num (k<num), só é divisivel por 1
else: 
    print("O número %d não é primo, pois contém mais de dois divisores." %(num))
#d < 1 tem mais de um divisor sem contar o próprio num
      
      