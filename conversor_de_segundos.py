# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:56:57 2024

@author: julia
"""

segundos = int(input("digite quando segundos você quer converter: "))

hora = segundos // 3600 
minutos = segundos // 60
seg = segundos%60 
resto_hora = minutos - (hora*60)
dias = segundos // 86460 

if (hora < 1) and (minutos >= 1):
    if minutos == 1:
        print("%d segundos dá: %d minuto e %d segundos." %(segundos,minutos,seg))
    if seg == 1:
        print("%d segundos dá: %d minutos e %d segundo." %(segundos,minutos,seg))
    if minutos == 1 and seg == 1:
        print("%d segundos dá: %d minuto e %d segundo." %(segundos,minutos,seg))
    if minutos != 1 and seg != 1:
        print("%d segundos dá: %d minutos e %d segundos." %(segundos,minutos,seg))
        
if minutos < 1:
    if segundos > 1 or segundos == 0:
        print("%d segundos dá: %d segundos." %(segundos,segundos))
    if segundos == 1:
        print("%d segundo dá: %d segundo." %(segundos,segundos))
    
if (hora >= 1) and (dias < 1):
    if hora == 1:
        if resto_hora == 1:
            print("%d segundos dá: %d hora, %d minuto e %d segundos" %(segundos,hora,resto_hora,seg))
        else:
            print("%d segundos dá: %d hora, %d minutos e %d segundos" %(segundos,hora,resto_hora,seg))
    elif hora != 1:
        if resto_hora == 1:
            print("%d segundos dá: %d horas, %d minuto e %d segundos" %(segundos,hora,resto_hora,seg))
        else:
            print("%d segundos dá: %d horas, %d minutos e %d segundos" %(segundos,hora,resto_hora,seg))
            
if hora >= 24:
    dias = segundos // 86400 
    horas = segundos // 3600
    resto_dia = horas - dias * 24
    minutos = (segundos - (horas * 3600))// 60
    seg = segundos - horas * 3600 - minutos * 60
    if dias == 1:
        print("%d segundos dá: %d dia, %d horas, %d minutos e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
    if dias == 1 and resto_dia == 1:
        print(print("%d segundos dá: %d dia, %d hora, %d minutos e %d segundos" %(segundos,dias,resto_dia,minutos,seg)))
    if dias == 1 and resto_dia == 1 and minutos == 1:
        print("%d segundos dá: %d dia, %d hora, %d minuto e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
    if dias == 1 and resto_dia == 1 and minutos == 1 and seg == 1:
        print("%d segundos dá: %d dia, %d hora, %d minuto e %d segundo" %(segundos,dias,resto_dia,minutos,seg))
    if resto_dia == 1:
        print("%d segundos dá: %d dias, %d hora, %d minutos e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
    if resto_dia == 1 and minutos == 1:
        print("%d segundos dá: %d dias, %d hora, %d minuto e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
    if resto_dia == 1 and minutos == 1 and seg == 1:
        print("%d segundos dá: %d dias, %d hora, %d minuto e %d segundo" %(segundos,dias,resto_dia,minutos,seg))
    if resto_dia == 1 and seg == 1:
        print("%d segundos dá: %d dias, %d hora, %d minutos e %d segundo" %(segundos,dias,resto_dia,minutos,seg))
    if minutos == 1:
        print("%d segundos dá: %d dias, %d horas, %d minuto e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
    if minutos == 1 and seg == 1:
        print("%d segundos dá: %d dias, %d horas, %d minuto e %d segundo" %(segundos,dias,resto_dia,minutos,seg))
    if seg == 1:
        print("%d segundos dá: %d dias, %d horas, %d minutos e %d segundo" %(segundos,dias,resto_dia,minutos,seg))
    if dias != 1 and resto_dia != 1 and minutos != 1 and seg != 1: 
        print("%d segundos dá: %d dias, %d horas, %d minutos e %d segundos" %(segundos,dias,resto_dia,minutos,seg))
#60 segundos = 1 minuto
#61 srgundos = 1 miuto e um segundo

#3600 = 1 hora
#1800 = meia hora

#1 dia = 86460 segundos
#2 dias, 3 horas, 4 minutos, 5 segundos

#172920 + 10800 + 240 + 5 = 183965 segundos

#dias = segundos // 86460 
#horas = segundos // 3600
#resto_dia = horas - dias * 24
#minutos = (segundos - (dia * 86460 + resto_dia * 3600)) // 60
#seg = segundos - (dia * 86460 + resto_dia * 3600 + minutos * 60)