# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:59:52 2024

@author: julia
"""

segundos = int(input("digite quando segundos você quer converter: "))

hora = segundos // 3600 
minutos = segundos // 60
seg = segundos%60 
resto_hora = minutos - (hora*60)
dias = segundos // 86460 

if (hora < 1) and (minutos >= 1):
    print("%d dias, %d horas, %d minutos e %d segundos." %(dias,hora,minutos,seg))
    
if minutos < 1:
    print("%d dias, %d horas, %d minutos e %d segundos." %(dias,hora,resto_hora,segundos))
    
if (hora >= 1) and (dias < 1):
    print("%d dias, %d horas, %d minutos e %d segundos." %(dias,hora,resto_hora,seg))
    
            
if hora >= 24:
    dias = segundos // 86400 
    horas = segundos // 3600
    resto_dia = horas - dias * 24
    minutos = (segundos - (horas * 3600))// 60
    seg = segundos - horas * 3600 - minutos * 60
    print("%d dias, %d horas, %d minutos e %d segundos." %(dias,resto_dia,minutos,seg))
          