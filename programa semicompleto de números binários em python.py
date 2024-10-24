# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:45:18 2024

@author: julia
"""
def main():
    
    def decimais_para_binários():
        def inicio():
            num = int(input("Digite um número: "))

            resultado = num
            resto = 0
            lista = []
            
            while resultado >= 1 and num != 0 and num != 1:
                if resultado == 1:
                    resto = 1
                else:
                    resto = resultado % 2   
                resultado = resultado // 2
                lista.append(resto)
            if num == 0:
                lista = [0]
            if num == 1:
                lista = [1]
                
            return(lista)
            
        def lista_nova(lista):
            tamanho = len(lista)
            tamanho = tamanho * -1
            i = 0
            listanova = []
            numero = 0
            
            while i != tamanho:
               i = i - 1 
               numero = lista[i]
               listanova.append(numero)
               
            return(listanova) 
                
      

        def formador_de_string(listanova):
            str_binario = ''
            tamanho = len(listanova)
            i = 0
            numero = 0
            while i < tamanho:
                numero = listanova[i]
                str_binario = str_binario + str(numero)
                i = i + 1
                
            print("Seu número corresponde à", str_binario, "em número binário")
            return(str_binario)
        
        formador_de_string(lista_nova(inicio()))
        
    def binários_para_decimais():
        num = int(input("Digite um número: "))
        clone = num
        tamanho = 1
        resultado = 0
        
        while resultado != num:
            resultado = num % 10**tamanho
            tamanho = tamanho + 1
            
            
        tamanho = tamanho - 1
        tam = tam2 = tamanho
        

        lista = []  
            
        
        while tam > 0:
            tam = tam - 1
            lista.append(clone % 10)
            clone = clone // 10
            
        soma = 0 
        expoente = 0
        t = 0
        while t < tam2:
            numero = lista[t]
            expoente = (2**t) * numero
            soma = soma + expoente 
            t = t + 1    
            
        print("Seu número corresponde à:", soma, "em número decimal")
        
        return(soma)
    
    print("Bem-Vindo(a)")
    print("")
    print("Este programa foi feito para converter decimais em binários ou vice-versa")
    print("")
    print("Escolha a opção desejada:")
    print("1- Converter decimal para binário")
    print("2- Converter binário em decimal")
    resposta = str(input(""))
    if resposta != "1" and resposta != "2":
        while resposta != "1" and resposta != "2":
            print("Resposta inválida")
            resposta = str(input(""))
    print()
    if resposta == "1":
        decimais_para_binários()
    if resposta == "2":
        binários_para_decimais()
    
            
    print("")
    print("Deseja converter mais um número?")
    print("1- Sim")
    print("2- Não")
    resp = str(input(""))
    if resp != "1" and resp != "2":
        while resp != "1" and resp != "2":
            print("Resposta inválida")
            resp = str(input(""))
    if resp == "1":
        main()
    if resp == "2":
        print("")
        print("Até a Próxima")
    
    
main()