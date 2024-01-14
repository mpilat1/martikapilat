# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:18:59 2023

@author: student
"""
import random

def sprawdz_czy_liczba_jest_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

losowa_liczba = random.randint(1, 1000)
wynik = sprawdz_czy_liczba_jest_parzysta(losowa_liczba)

if wynik:
    print(f"Liczba {losowa_liczba} jest parzysta.")
else:
    print(f"Liczba {losowa_liczba} jest nieparzysta.")