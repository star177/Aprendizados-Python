# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:25:43 2024

@author: julia
"""


def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 != 0):
        return("Fizz")
    if n % 5 == 0 and (n % 3 != 0):
        return("Buzz")
    if (n % 3 == 0) and (n % 5 == 0):
        return("FizzBuzz")
    else: 
        return(n)
    