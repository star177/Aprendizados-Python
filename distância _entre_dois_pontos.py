# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:22:40 2024

@author: julia
"""
print("Saiba a distância entre dois pontos num plano cartesiano (x,y): ")
print()
print("Escreva os pontos sem parênteses e separados por pontos. Ex:")
print("x.y")
print()
xy_1 = float(input("digite o primeiro ponto: "))
xy_2 = float(input("digite o segundo ponto: "))

x_1 = ((xy_1*10) // 10)
y_1 = ((xy_1*10) % 10)
x_2 = ((xy_2*10) // 10)
y_2 = ((xy_2*10) % 10)

d = ((((x_1 - x_2)**2) + ((y_1 - y_2)**2))**(1/2))

if (d * 10) % 10 != 0:
    print("A distância entre os pontos (%d,%d) e (%d,%d) é:" %(x_1,y_1,x_2,y_2), d)
else:
    d = int(d)
    print("A distância entre os pontos (%d,%d) e (%d,%d) é %d" %(x_1,y_1,x_2,y_2,d))