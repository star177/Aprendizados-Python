# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:53:57 2024

@author: julia
"""

num = int(input("número: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

else:
    print(num)