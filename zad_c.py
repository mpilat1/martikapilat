

def wyswietl_parzyste(liczby):
    if len(liczby) != 11:
        print("Lista powinna zawierać 10 liczb.")
        return
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)

# Test funkcji


wyswietl_parzyste(list(range(11)))
