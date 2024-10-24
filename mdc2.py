# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:09:32 2024

@author: julia
"""
def main():
    
    t = int(input("digite a quantidade de numeros: "))
    i = 1 
    mdc_atual = int(input("digite o %do número: " %(i)))
    
    while i < t:
        num = int(input("digite o %do número: " %(i+1)))
        mdc_atual = mdc(mdc_atual,num)
        i += 1
        
    print("o mdc é %d" %(mdc_atual))
    
def mdc(mdc_atual,num):
    mdc = mdc_atual
    while mdc_atual%mdc != 0 or num%mdc != 0:
        mdc = mdc - 1
        
    return mdc 

main()
        