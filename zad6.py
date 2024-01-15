# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:31:23 2023

@author: student
"""

def zlaczenie_list(lista_1, lista_2):
    polaczona_lista = lista_1 + lista_2
    polaczona_lista = list(set(polaczona_lista))
    
    wynik_listy = [i ** 3 for i in polaczona_lista]
    
    return wynik_listy


lista_1 = [9, 8, 7, 6, 5]
lista_2 = [1, 2, 3, 4, 5]

wynik = zlaczenie_list(lista_1, lista_2)
print(wynik)