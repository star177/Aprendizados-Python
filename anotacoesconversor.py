# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:02:06 2024

@author: julia
"""
#--------------------------
60 segundos = 1 minuto
61 srgundos = 1 miuto e um segundo

3600 = 1 hora
1800 = meia hora

1 dia = 86460 segundos
2 dias, 3 horas, 4 minutos, 5 segundos

172920 + 10800 + 240 + 5 = 183965 segundos

dias = segundos // 86460 
horas = segundos // 3600
resto_dia = horas - dias * 24
minutos = (segundos - (dia * 86460 + resto_dia * 3600)) // 60
seg = segundos - (dia * 86460 + resto_dia * 3600 + minutos * 60)

RESPOSTA = 183965 SEGUNDOS ->2 DIAS, 3 HORAS, 4 MINUTOS E 5 SEGUNDOS
#--------------------------