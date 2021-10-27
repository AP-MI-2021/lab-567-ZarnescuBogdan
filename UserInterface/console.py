import datetime

from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitate1 import stergeToateCheltuielile
from Logic.functionalitate2 import adunaValoareCheltuieliDupaData
from Logic.functionalitate3 import celeMaiMariCheltuieli
from Logic.functionalitate4 import ordonareDescrescatorDupaSuma
from Logic.functionalitate5 import sumeLunarePerApartament


def printMenu():
    print('1. Adaugare cheltuiala.')
    print('2. Stergere cheltuiala.')
    print('3. Modificare cheltuiala.')
    print('4. Stergere cheltuieli pentru un apartament dat.')
    print('5. Adunare valoare data la toate cheltuielile dintr-o data.')
    print('6. Afisare cele mai mari cheltuieli pentru fiecare tip de cheltuiala.')
    print('7. Ordonare cheltuieli descrescator dupa suma.')
    print('8. Afisare sume lunare pentru fiecare apartament.')
    print('a. Afisare cheltuieli.')
    print('x. Iesire.')


def readDate():
    try:
        givenString = input('Dati data, cu elementele separate printr-o liniuta: ')
        numbersAsString = givenString.split('-')
        year = int(numbersAsString[0])
        month = int(numbersAsString[1])
        day = int(numbersAsString[2])
        return datetime.date(year, month, day)
    except ValueError as ve:
        print(f'Error: {ve}')
        return None


def uiAdaugaCheltuiala(lista):
    try:
        id = input('Dati id-ul: ')
        nrApartament = int(input('Dati nr. apartamentului: '))
        suma = float(input('Dati suma: '))
        data = readDate()
        if data is None:
            raise ValueError('Data nu a fost introdusa corespunzator!')
        tip = input('Dati tipul: ')
        return adaugaCheltuiala(id, nrApartament, suma, data, tip, lista)
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeCheltuiala(lista):
    id = input('Dati id-ul cheltuielii de sters: ')
    return stergeCheltuiala(id, lista)


def uiModificaCheltuiala(lista):
    try:
        id = input('Dati id-ul cheltuielii de modificat: ')
        nrApartament = int(input('Dati noul nr. de apartament: '))
        suma = float(input('Dati noua suma: '))
        data = readDate()
        if data is None:
            raise ValueError('Data nu a fost introdusa corespunzator!')
        tip = input('Dati noul tip: ')
        return modificaCheltuiala(id, nrApartament, suma, data, tip, lista)
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeToateCheltuielile(lista):
    try:
        nrApartament = int(input('Dati nr. de apartament pentru care trebuie sterse toate cheltuielile: '))
        return stergeToateCheltuielile(nrApartament, lista)
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdunaValoareCheltuieliDupaData(lista):
    try:
        data = readDate()
        if data is None:
            raise ValueError('Data nu a fost introdusa corespunzator!')
        valoare = float(input(f'Dati valoarea care trebuie adunata la cheltuielile din data {data}: '))
        return adunaValoareCheltuieliDupaData(data, valoare, lista)
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiCeleMaiMariCheltuieli(lista):
    rezultat = celeMaiMariCheltuieli(lista)
    for tip in rezultat:
        print('Tipul {} are suma maxima {}'.format(tip, rezultat[tip]))


def uiOrdonareDescrescatorDupaSuma(lista):
    showAll(ordonareDescrescatorDupaSuma(lista))


def uiSumeLunarePerApartament(lista):
    rezultat = sumeLunarePerApartament(lista)
    for nrApartament in rezultat:
        for an in rezultat[nrApartament]:
            for luna in rezultat[nrApartament][an]:
                print('Apartamentul cu numarul {} are cheltuieli lunare in anul {}, luna {} in valoare de {}'.format(
                    nrApartament,
                    an,
                    luna,
                    rezultat[nrApartament][an][luna]))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input('Dati optiunea: ')

        if optiune == '1':
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == '2':
            lista = uiStergeCheltuiala(lista)
        elif optiune == '3':
            lista = uiModificaCheltuiala(lista)
        elif optiune == '4':
            lista = uiStergeToateCheltuielile(lista)
        elif optiune == '5':
            lista = uiAdunaValoareCheltuieliDupaData(lista)
        elif optiune == '6':
            uiCeleMaiMariCheltuieli(lista)
        elif optiune == '7':
            uiOrdonareDescrescatorDupaSuma(lista)
        elif optiune == '8':
            uiSumeLunarePerApartament(lista)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reincercati: ')
