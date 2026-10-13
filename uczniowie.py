from pathlib import Path

PLIK = Path("uczniowie.txt")


def wczytaj_dane(plik):
    with open(plik, "r", encoding="utf-8") as plik:
        dane = []
        for linia in plik:
            czysta = linia.strip()
            if czysta != "":
                dane.append(czysta)
    return dane


def wyswietl_menu():
    print("\nMENU")
    print("1. Wyświetl listę uczniów")
    print("2. Posortuj listę alfabetycznie")
    print("3. Usuń ucznia z listy")
    print("4. Zakończ program")


def wyswietl_dane(dane):
    print("\nLista uczniów:")
    if not dane:
        print("Lista jest pusta")
    else:
        for element in dane:
            print(element)


def posortuj_dane(dane):
    dane.sort(key=str.casefold)
    with open(PLIK, "w", encoding="utf-8") as plik:
        for element in dane:
            plik.write(element + "\n")
    print("Lista zostala posortowana alfabetycznie")


def usun_ucznia(dane):
    wyswietl_dane(dane)

    if not dane:
        return

    uczen = input("Podaj imie i nazwisko ucznia do usuniecia: ").strip()

    for element in dane:
        if element.casefold() == uczen.casefold():
            dane.remove(element)
            with open(PLIK, "w", encoding="utf-8") as plik:
                for uczen in dane:
                    plik.write(uczen + "\n")
            print("Uczen zostal usuniety z listy")
            return

    print("Nie znaleziono takiego ucznia")


def main():
    try:
        dane = wczytaj_dane(PLIK)
    except FileNotFoundError:
        print("Nie znaleziono pliku uczniowie.txt")
        return

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcje 1-4: ").strip()

        if wybor == "1":
            wyswietl_dane(dane)
        elif wybor == "2":
            posortuj_dane(dane)
        elif wybor == "3":
            usun_ucznia(dane)
        elif wybor == "4":
            print("Koniec programu")
            break
        else:
            print("Niepoprawny wybor Wybierz opcje od 1 do 4")


main()
