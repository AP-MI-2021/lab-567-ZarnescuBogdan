import datetime

from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitate1 import stergeToateCheltuielile


def printMenu():
    print('1. Adaugare cheltuiala.')
    print('2. Stergere cheltuiala.')
    print('3. Modificare cheltuiala.')
    print('4. Stergere cheltuieli pentru un apartament dat.')
    print('a. Afisare cheltuieli.')
    print('x. Iesire.')


def readDate():
    givenString = input('Dati data, cu elementele separate printr-o liniuta: ')
    numbersAsString = givenString.split('-')
    year = int(numbersAsString[0])
    month = int(numbersAsString[1])
    day = int(numbersAsString[2])
    return datetime.date(year, month, day)


def uiAdaugaCheltuiala(lista):
    nrApartament = int(input('Dati nr. apartamentului: '))
    suma = float(input('Dati suma: '))
    data = readDate()
    tip = input('Dati tipul: ')
    return adaugaCheltuiala(nrApartament, suma, data, tip, lista)


def uiStergeCheltuiala(lista):
    nrApartament = int(input('Dati nr. de apartament al cheltuielii de sters: '))
    return stergeCheltuiala(nrApartament, lista)


def uiModificaCheltuiala(lista):
    nrApartament = int(input('Dati nr. de apartament al cheltuielii de modificat: '))
    suma = float(input('Dati noua suma: '))
    data = readDate()
    tip = input('Dati noul tip: ')
    return modificaCheltuiala(nrApartament, suma, data, tip, lista)


def uiStergeToateCheltuielile(lista):
    nrApartament = int(input('Dati nr. de apartament pentru care trebuie sterse toate cheltuielile: '))
    return stergeToateCheltuielile(nrApartament, lista)


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


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
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reincercati: ')