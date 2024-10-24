# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:02:10 2024

@author: julia
"""

x_1 = int(input("digite o x1: "))
y_1 = int(input("digite o y1: "))
x_2 = int(input("digite o x2: "))
y_2 = int(input("digite o y2: "))

d = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**(1/2)

print("A distância entre os pontos é de:", d)