
def pomnoz_przez_dwa_z_for(lista_liczb):
    nowa_lista = []
    for liczba in lista_liczb:
        nowa_lista.append(liczba * 2)
    return nowa_lista

# sprawdzenie czy działa


lista_liczb = [10, 11, 55, 47, 33]

wynik_for = pomnoz_przez_dwa_z_for(lista_liczb)
print(wynik_for)
