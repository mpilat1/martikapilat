
def wyswietl_imiona(lista_imion):
    if len(lista_imion) != 5:
        print("Lista imion musi zawierać dokładnie 5 imion.")
    else:
        for imie in lista_imion:
            print(imie)


lista_imion = ["Jacek", "Lukasz", "Michal", "Agnieszka", "Laura"]
wyswietl_imiona(lista_imion)
