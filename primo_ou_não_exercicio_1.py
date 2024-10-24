# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:45:34 2024

@author: julia
"""

num = int(input("coloque um número: "))
num_salvo = num
i = 1
primo = False
d = 0
while i < num: 
    if num % i == 0 :
        d = d + 1
    i = i + 1
if d == 1:
    print("primo")
else:
    print("não primo")
    
    