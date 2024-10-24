# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:01:34 2024

@author: julia
"""

#Conceitos úteis

#atribuir valor a várias variáveis:
x, y = 10, 20

print(x)
print(y)



def funcao():
    return(77, 1.83)
   
peso, altura = funcao()
print(peso)
print(altura)



x, y = y, x
print(x)
print(y)


#Operações:
x += 10 #x = x + 10
x *= 2 #x = x * 2
#etc


#parametro opcional:
    
def pagamento_semanal(valor_por_hora, num_horas = 40):
    return(valor_por_hora * num_horas)

print(pagamento_semanal(100, 36))
print(pagamento_semanal(100))

    
#Assert

def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >= 0 and num_horas >= 0
    return(valor_por_hora * num_horas)

print(pagamento_semanal(100, -36))
    