# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:29:06 2023

@author: student
"""

def sprawdz_wartosc_w_liscie(lista, wartosc):
    if wartosc in lista:
        return True
    else: 
        return False
    
lista_1 = [7, 8, 9, 10, 11, 12]
wartosc = 10
wynik = sprawdz_wartosc_w_liscie(lista_1, wartosc)
print(wynik)