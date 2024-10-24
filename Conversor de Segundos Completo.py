# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:31:31 2024

@author: julia
"""

#conversor 

def conv(sec):
    segundos = sec
    dias = sec//86400
    sec = sec-(86400*dias)
    horas = sec//3600
    sec = sec-(3600*horas)
    minutos = sec//60
    sec = sec-(60*minutos)
    
    #resposta
    
    def resposta(segundos, dias, horas, minutos, sec):
        
        resposta = ''
        
        #dias
        if dias == 1:
            resposta = '1 dia '
        if dias > 1:
            resposta = str(dias) + ' dias '
            
        #horas
        if horas == 1:
            resposta = resposta + '1 hora '
        if horas > 1:
            resposta = resposta + str(horas) + ' horas '
            
        #minutos:
        if minutos == 1:
            resposta = resposta + '1 minuto '
        if  minutos > 1:
            resposta = resposta + str(minutos) + ' minutos '
            
        #segundos
        if sec == 0:
            resposta = resposta.strip() + '.'
        if sec == 1:
            resposta = resposta + 'e 1 segundo.'
        if sec > 1:
            resposta = resposta + 'e ' + str(sec) + ' segundos.'
        
        resposta = str(segundos) + ' segundos são ' + resposta
        
        return(resposta)
        
    print(resposta(segundos, dias, horas, minutos, sec))

#main
def main():
    print('Conversor de segundos para dias, horas, minutos e segundos')
    print()
    sec = int(input("Segundos: "))
    while sec <= 0:
        print("Tente Novamente")
        sec = int(input("Segundos: "))
    conv(sec)

main()